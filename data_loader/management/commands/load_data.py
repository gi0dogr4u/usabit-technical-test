import asyncio
from datetime import datetime
import aiohttp
import pandas as pd
from data_loader.models import CityWeather
from django.conf import settings
from django.core.management.base import BaseCommand
from asgiref.sync import sync_to_async


API_URL = 'https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={key}&units=metric'

class Command(BaseCommand):
    help = 'Load city weather data from CSV and update temperature using OpenWeather API asynchronously'

    def handle(self, *args, **kwargs):
        file_path = 'cities.csv'
        df = pd.read_csv(file_path)
        cities = df['City ID'].tolist()
        asyncio.run(self.fetch_weather_data(cities))

    async def fetch_weather_data(self, cities):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_and_save_city_weather(session, city_id) for city_id in cities]
            await asyncio.gather(*tasks)

    async def fetch_and_save_city_weather(self, session, city_id):
        url = API_URL.format(city_id=city_id, key=settings.OPENWEATHER_API_KEY)

        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    city_name = data['name']
                    temperature = data['main']['temp']

                    await sync_to_async(self.update_or_create_city_weather)(city_id, city_name, temperature)
                    self.stdout.write(self.style.SUCCESS(f'Successfully updated city {city_name}'))
                else:
                    self.stdout.write(self.style.ERROR(f'Failed to fetch data for city ID {city_id}, status code: {response.status}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error fetching data for city ID {city_id}: {str(e)}'))


    # Método separado para atualização no banco de dados
    def update_or_create_city_weather(self, city_id, city_name, temperature):
        CityWeather.objects.update_or_create(
            city_id=city_id,
            defaults={
                'city_name': city_name,
                'temperature': temperature,
                'last_updated': datetime.now()
            }
        )
