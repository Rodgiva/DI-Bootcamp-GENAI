import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(command="mcp", args=["run", "server.py"], env=None)


def extract_content(payload):
    """Best-effort to pull text from MCP responses."""
    if hasattr(payload, "contents"):
        contents = payload.contents
        if contents:
            first = contents[0]
            if hasattr(first, "text"):
                return first.text
            if isinstance(first, dict) and "text" in first:
                return first["text"]
            return str(first)
    if hasattr(payload, "content"):
        return payload.content
    return str(payload)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # TODO: list resources and print their URIs
            resources = await session.list_resources()
            print("Resources:")
            for r in resources.resources:
                print(" -", r.uri)

            templates = await session.list_resource_templates()
            print("Resource templates:")
            for t in templates.resourceTemplates:
                print(" -", t.uriTemplate)

            # TODO: list tools and print their names
            tools = await session.list_tools()
            print("Tools:")
            for t in tools.tools:
                print(" -", t.name)

            # TODO: read greeting://hello and print the content
            resource = await session.read_resource("greeting://Avi")
            print("Greeting:", extract_content(resource))

            # TODO: call add with a=1, b=7 and print the result
            result = await session.call_tool("add", arguments={"a": 1, "b": 7})
            print("Add result:", result.content[0].text)

if __name__ == "__main__":
    asyncio.run(run())