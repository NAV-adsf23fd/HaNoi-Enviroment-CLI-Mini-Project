from rich.table import Table
from rich.console import Console
from weather import get_weather, describe_weather
from air import get_air_quality, color_aqi


# Warning 
def warning_message(aqi: int):
    if aqi > 150:
        return "[bold red]CẢNH BÁO: Hạn chế ra ngoài![/bold red]"
    elif aqi > 100:
        return "[bold yellow]CẢNH BÁO: Nên đeo khẩu trang![/bold yellow]"
    return ""


def main():
    console = Console()

    weather = get_weather() or {}
    air = get_air_quality() or {}

    table = Table(title="Hà Nội hiện tại")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="bold")

    # Weather
    temperature = weather.get("temperature")
    windspeed = weather.get("windspeed")
    weathercode = weather.get("weathercode", -1)
    description = describe_weather(weathercode)

    table.add_row("Điều kiện thời tiết", description)
    table.add_row("Nhiệt độ (°C)", str(temperature))
    table.add_row("Tốc độ gió (km/h)", str(windspeed))

    # Air
    pm25 = air.get("pm2_5")
    pm10 = air.get("pm10")
    aqi = air.get("us_aqi", 0)

    table.add_row("Bụi PM2.5 (µg/m³)", str(pm25))
    table.add_row("Bụi PM10 (µg/m³)", str(pm10))
    table.add_row("Chỉ số US AQI", color_aqi(aqi))

    console.print('\n')
    console.print(table)

    # Warning
    warning = warning_message(aqi)
    if warning:
        console.print(' ', warning)
    console.print('\n')


if __name__ == "__main__":
    main()