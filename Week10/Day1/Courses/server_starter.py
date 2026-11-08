"""
server_starter.py — Day 1: Live-coding starting point

The instructor builds the tools from scratch during the lecture.
When finished, the result will look like server.py (which you can study after class).

Run it:
    python server_starter.py

Steps to follow along:
  1. Run this file — the server starts with no tools
  2. Add read_file (instructor leads)
  3. Add get_weather (instructor leads)
  4. See all three primitives in server.py at the end
"""

import sys
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Workshop")


# ─── Add your tools here ──────────────────────────────────────────────────────
#
# Pattern:
#   @mcp.tool()
#   def tool_name(param: str) -> str:
#       """What this tool does and WHEN the LLM should call it."""
#       # your code here
#       return "result as a string"
#

@mcp.tool()
def read_file(filename: str) -> str:
    """Read any text file from the current directory and return its full content."""
    path = Path(__file__).parent / filename
    if not path.exists():
        return f"File not found: {filename}" # return a string, never raise an error
    return path.read_text(encoding="utf-8")

@mcp.tool()
def get_weather(city: str) -> str:
    """Get the current weather condition and temperature for any city in the world."""

    import requests
    try:
        r = requests.get(f"https://wttr.in/{city}?format=3", timeout=5)
        r.raise_for_status()
        return r.text.strip()          # e.g. "Tel Aviv: ⛅️  +28°C"
    except Exception:
        pass                           # wttr.in down/blocked → try Open-Meteo

    try:
        geo = requests.get("https://geocoding-api.open-meteo.com/v1/search",
                           params={"name": city, "count": 1}, timeout=5).json()
        if not geo.get("results"):
            return f"City not found: {city}"
        place = geo["results"][0]
        wx = requests.get("https://api.open-meteo.com/v1/forecast",
                          params={"latitude": place["latitude"],
                                  "longitude": place["longitude"],
                                  "current": "temperature_2m,wind_speed_10m"},
                          timeout=5).json()["current"]
        return (f"{place['name']}: {wx['temperature_2m']:+.0f}°C, "
                f"wind {wx['wind_speed_10m']} km/h")
    except Exception as e:
        return f"Weather unavailable: {e}"

@mcp.resource("note://today")
def today_notes() -> str:
    """Workshop notes for today. A host app like Goose read this on startup to give the LLM background context without the user having to ask."""
    path = Path(__file__).parent / "notes.txt"
    if not path.exists():
        return f"File not found."
    return path.read_text(encoding="utf-8")

@mcp.prompt(name="summarize")
def summarize_prompt(filename: str) -> str:
    """Prompt ramplate: instruct the LLm to read file and summarize it. The user trigger this by selecting 'summarize' on the client like Goose."""
    return(
        f"Please read the file '{filename}' using the read_file tool, then write a brief, clear summery of its contents."
    )

# ─── Server entry point (leave this as-is) ────────────────────────────────────

if __name__ == "__main__":
    if sys.stdin.isatty():
        print("Server starting → http://127.0.0.1:8000/mcp/", file=sys.stderr)
        mcp.run(transport="streamable-http")
    else:
        mcp.run()