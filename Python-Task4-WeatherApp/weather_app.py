import urllib.request
import urllib.parse
import json

def get_weather(city_name):
    # Public Open-Meteo geocoding and weather APIs (no external API key required)
    try:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={urllib.parse.quote(city_name)}&count=1&language=en&format=json"
        req = urllib.request.Request(geo_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            geo_data = json.loads(response.read().decode('utf-8'))

        if "results" not in geo_data or len(geo_data["results"]) == 0:
            print(f"Error: City '{city_name}' not found. Please verify the spelling.")
            return

        location = geo_data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        resolved_name = location.get("name", city_name)
        country = location.get("country", "")

        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
            f"&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
        )
        req_weather = urllib.request.Request(weather_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_weather, timeout=10) as weather_resp:
            weather_data = json.loads(weather_resp.read().decode('utf-8'))

        current = weather_data.get("current", {})
        temp_c = current.get("temperature_2m")
        temp_f = (temp_c * 9/5) + 32 if temp_c is not None else None
        humidity = current.get("relative_humidity_2m")
        wind_speed = current.get("wind_speed_10m")
        weather_code = current.get("weather_code", 0)

        # Basic weather condition code interpretation
        conditions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Light drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snow fall",
            95: "Thunderstorm"
        }
        condition_desc = conditions.get(weather_code, "Fair / Moderate")

        print("\n" + "=" * 45)
        print(f" Weather Report: {resolved_name}, {country}")
        print("=" * 45)
        print(f"Condition   : {condition_desc}")
        print(f"Temperature : {temp_c}°C ({temp_f:.1f}°F)")
        print(f"Humidity    : {humidity}%")
        print(f"Wind Speed  : {wind_speed} km/h")
        print("=" * 45)

    except urllib.error.URLError:
        print("Error: Network error. Please check your internet connection.")
    except Exception as e:
        print(f"Error: An unexpected error occurred ({e}).")

def main():
    print("=" * 45)
    print("           REAL-TIME WEATHER APP             ")
    print("=" * 45)

    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()
        if not city:
            print("Error: Input cannot be empty. Please enter a city name.")
            continue
        if city.lower() in ['quit', 'exit', 'q']:
            print("\nThank you for using the Weather App!")
            break

        get_weather(city)

if __name__ == "__main__":
    main()
