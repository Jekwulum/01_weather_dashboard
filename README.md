# 30 Days DevOps Challenge - Weather Dashboard
Day 1: Building a weather data collection system using Azure Blob storage and OpenWeather API

# Weather Data Collection System - DevOps Day 1 Challenge

## Project Overview
WeatherDashboard is a Python application that fetches weather data for specified cities using the OpenWeather API and stores the data in Azure Blob Storage for further analysis or use. This project demonstrates core DevOps principles by combining:

- External API Integration (OpenWeather API)
- Cloud Storage (Azure Blob storage)
- Infrastructure as Code
- Version Control (Git)
- Python Development
- Error Handling
- Environment Management

## Features
- Fetches real-time weather data from the OpenWeather API
- Stores weather data in Azure Blob Storage in JSON format
- Automatically creates the necessary Azure Blob container if it doesn't exist
- Includes timestamped data for tracking changes over time
- Supports multiple cities tracking

## Prerequisites
- Python 3.x
- Azure Storage Account credentials
- OpenWeather API key

## Dependencies
- python-dotenv
- requests
- azure-storage-blob

## Project Striucture
```shell
01_weather_dashboard/g
├── src/
│   ├── __init__.py
│   └── weather_dashboard.py
├── tests/
├── data/
├── .gitignore
├── .env
├── requirements.txt
└── README.md
```

## Running the application
1. Clone the repository
    ```shell
    git clone git@github.com:Jekwulum/01_weather_dashboard.git
    cd 01_weather_dashboard
    ```
2. Create a virtual environment:
   ```shell
   python -m venv .venv
   source .venv/Scripts/activate  # On Windows use `.venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```shell
   pip install -r requirements.txt
   ```
4. Configure environment variables (.env):
   ```shell
   OPENWEATHER_API_KEY=your_api_key
   AZURE_STORAGE_CONNECTION_STRING=your_storage_account_connection_string
   ```
5. Run the application:
   ```shell
   python src/weather_dashboard.py
   ```

## What I learned
Azure Blob storage container creation and management
Environment variable management for secure API keys
Python best practices for API integration
Git workflow for project development
Error handling in distributed systems
Cloud resource management

## Future Enhancements
Add weather forecasting
Implement data visualization
Add more cities
Create automated testing
Set up CI/CD pipeline