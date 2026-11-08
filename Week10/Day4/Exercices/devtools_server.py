"""Custom MCP server: test runner / linter for the sandbox repo."""
import subprocess, sys
from pathlib import Path
# from fastmcp import FastMCP
from mcp.server.fastmcp import FastMCP

REPO = Path(__file__).parent / "sandbox"
mcp = FastMCP(name="devtools")

def _run(args, timeout=120):
    p = subprocess.run(args, cwd=REPO, capture_output=True, text=True, timeout=timeout)
    return p.returncode, (p.stdout + p.stderr).strip()[-4000:]

@mcp.tool()
def ping() -> str:
    """Health check tool."""
    return "pong"

@mcp.tool()
def run_pytest(test_path: str = "") -> str:
    """Run the project's pytest suite. Optionally restrict to one file or test id."""
    args = [sys.executable, "-m", "pytest", "-q", "--no-header"]
    if test_path:
        args.append(test_path)
    rc, out = _run(args)
    return f"exit_code={rc} ({'PASS' if rc == 0 else 'FAIL'})\n\n{out}"

@mcp.tool()
def run_ruff(fix: bool = False) -> str:
    """Lint the project with ruff. Set fix=True to auto-apply safe fixes."""
    args = [sys.executable, "-m", "ruff", "check", "."]
    if fix:
        args.append("--fix")
    rc, out = _run(args)
    return f"exit_code={rc}\n\n{out or 'no issues found'}"

@mcp.tool()
def project_health() -> str:
    """Read-only summary of the repo: file count, test status, lint status. Modifies nothing."""
    py = sorted(p.relative_to(REPO).as_posix() for p in REPO.rglob("*.py") if ".git" not in p.parts)
    rc_t, out_t = _run([sys.executable, "-m", "pytest", "-q", "--no-header"])
    rc_l, _ = _run([sys.executable, "-m", "ruff", "check", "."])
    return (f"python_files={len(py)}: {py}\n"
            f"tests={'PASS' if rc_t == 0 else 'FAIL'}\n"
            f"lint={'CLEAN' if rc_l == 0 else 'ISSUES'}\n"
            f"last_test_output:\n{out_t[-800:]}")

if __name__ == "__main__":
    mcp.run(transport="stdio")
