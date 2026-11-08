from mcp.server.fastmcp import FastMCP

mcp = FastMCP("WeatherDemo")

@mcp.tool()
def get_weather(city: str) -> dict:
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

@mcp.resource("greeting://{name}")
def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("server is runing...")
    mcp.run(transport="stdio")