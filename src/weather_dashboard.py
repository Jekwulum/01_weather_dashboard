import os
import json
import requests
from azure.storage.blob import BlobServiceClient
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class WeatherDashboard:
  def __init__(self):
    """Initialize the WeatherDashboard with necessary configurations and Blob Storage setup."""
    self.api_key = os.getenv("OPENWEATHER_API_KEY")
    self.connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    
    self.container_name = "weather-data"
    self.blob_service_client = BlobServiceClient.from_connection_string(self.connect_str)
    self._create_container_if_not_exists()
  
  def _create_container_if_not_exists(self):
    """Ensure the Blob container exists, creating it if necessary."""
    container_client = self.blob_service_client.get_container_client(self.container_name)
    if not container_client.exists():
      container_client.create_container()
      print(f"Container '{self.container_name}' created.")

  def upload_to_blob(self, weather_data, city):
    """upload data to blob"""
    if not weather_data:
      return False
    
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    file_name = f"weather-data/{city}-{timestamp}.json"
    
    try:
      weather_data['timestamp'] = timestamp
      blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=file_name)
      blob_client.upload_blob(json.dumps(weather_data), overwrite=True)
      print(f"FIle '{file_name}' uploaded to container '{self.container_name}'")
      return True
    except Exception as e:
      print(f"Error uploading blob for {city}: {e}")
      return False

  def fetch_weather_data(self, city):
    """Fetch weather data from OpenWeather API"""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
            "q": city,
            "appid": self.api_key,
            "units": "imperial"
        }
    
    try:
      response = requests.get(base_url, params=params)
      response.raise_for_status()
      return response.json()
    except requests.exceptions.RequestException as e:
      print(f"Error fetching weather data: {e}")
      return None


def main():
  """Program entry point"""
  dashboard = WeatherDashboard()

  cities = ["Philadelphia", "Seattle", "Lagos", "London", "Bozeman"]

  for city in cities:
    print(f"\nFetching weather for {city}...")
    weather_data = dashboard.fetch_weather_data(city)
    if weather_data:
      temp = weather_data['main']['temp']
      feels_like = weather_data['main']['feels_like']
      humidity = weather_data['main']['humidity']
      description = weather_data['weather'][0]['description']

      print(f"Temperature: {temp}°F")
      print(f"Feels like: {feels_like}°F")
      print(f"Humidity: {humidity}%")
      print(f"Conditions: {description}")

      success = dashboard.upload_to_blob(weather_data, city)
      if success:
        print(f"Weather data for {city} saved to {dashboard.container_name}")
    else:
      print(f"Failed to fetch weather data for {city}")

if __name__ == '__main__':
  main()