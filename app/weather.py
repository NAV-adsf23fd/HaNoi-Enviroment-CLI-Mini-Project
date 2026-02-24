import requests

LATITUDE = 21.03
LONGITUDE = 106.85

def get_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LATITUDE}&longitude={LONGITUDE}"
        "&current_weather=true"
    )
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("current_weather")
    except requests.exceptions.RequestException as e:
        print("API request error:", e)
        return None


# Weather description
def describe_weather(code: int):
    if code == 0:
        return "Trời nắng"
    elif code in [1, 2, 3]:
        return "Có mây"
    elif code in [45, 48]:
        return "Sương mù"
    elif code in [51, 53, 55]:
        return "Mưa nhẹ"
    elif code in [61, 63, 65]:
        return "Mưa"
    elif code == 95:
        return "Giông"
    else:
        return "Không rõ"