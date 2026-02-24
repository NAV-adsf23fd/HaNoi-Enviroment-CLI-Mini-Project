# Hanoi Environment CLI

CLI hiển thị **thời tiết** và **chất lượng không khí (AQI, PM2.5, PM10)** tại Hà Nội.
Dữ liệu lấy từ Open-Meteo APIs và in ra terminal bằng rich.

## Tính năng
- Nhiệt độ, tốc độ gió hiện tại
- PM2.5, PM10, US AQI
- Chạy trong Docker

## Yêu cầu
- Docker

## Chạy bằng Docker
```bash
docker build -t hanoi-env-cli .
docker run hanoi-env-cli