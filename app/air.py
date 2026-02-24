import requests

LATITUDE = 21.03
LONGITUDE = 106.85

def get_air_quality():
    url = (
        "https://air-quality-api.open-meteo.com/v1/air-quality"
        f"?latitude={LATITUDE}&longitude={LONGITUDE}"
        "&current=us_aqi,pm10,pm2_5"
    )
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("current")
    except requests.exceptions.RequestException as e:
        print("API request error:", e)
        return None


# AQI color
def color_aqi(aqi: int):
    if aqi <= 50:
        return f"[green]{aqi} (Tốt)[/green]"
    elif aqi <= 100:
        return f"[yellow]{aqi} (Trung bình)[/yellow]"
    elif aqi <= 150:
        return f"[orange1]{aqi} (Kém)[/orange1]"
    elif aqi <= 200:
        return f"[red]{aqi} (Xấu)[/red]"
    else:
        return f"[purple]{aqi} (Rất xấu)[/purple]"