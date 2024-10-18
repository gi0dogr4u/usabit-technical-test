from django.db import models


class CityWeather(models.Model):
    city_id = models.IntegerField(unique=True, default=0)
    city_name = models.CharField(max_length=100)
    temperature = models.FloatField()
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city_name} - {self.temperature}°C"