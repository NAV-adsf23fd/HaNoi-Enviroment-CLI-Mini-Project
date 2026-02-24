# Hanoi Environment CLI

A CLI that displays **weather** and **air quality (AQI, PM2.5, PM10)** in Hanoi.
Data is fetched from the Open-Meteo APIs and rendered in the terminal using rich.

## Features
- Current temperature and wind speed
- PM2.5, PM10, US AQI
- Runs in Docker

## Requirements
- Docker

## Run with Docker
```bash
docker build -t hanoi-env-cli .
docker run hanoi-env-cli