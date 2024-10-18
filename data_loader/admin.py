from django.contrib import admin
from .models import CityWeather


class TemperatureStatusFilter(admin.SimpleListFilter):
    title = 'Status da Temperatura'
    parameter_name = 'temperature_status'

    def lookups(self, request, model_admin):
        """Define as opções de filtragem."""
        return [
            ('cold', 'Frio'),
            ('mild', 'Ameno'),
            ('warm', 'Quente'),
            ('hot', 'Muito Quente'),
        ]

    def queryset(self, request, queryset):
        """Filtra os resultados com base na temperatura."""
        if self.value() == 'cold':
            return queryset.filter(temperature__lt=0)
        elif self.value() == 'mild':
            return queryset.filter(temperature__gte=0, temperature__lt=20)
        elif self.value() == 'warm':
            return queryset.filter(temperature__gte=20, temperature__lt=30)
        elif self.value() == 'hot':
            return queryset.filter(temperature__gte=30)
        return queryset


@admin.register(CityWeather)
class CityWeatherAdmin(admin.ModelAdmin):
    list_display = ('city_id', 'city_name', 'temperature', 'last_updated', 'temperature_status')

    list_filter = ('last_updated', TemperatureStatusFilter)

    search_fields = ('city_name', 'city_id')

    # Método para agregar informações de forma intuitiva
    def temperature_status(self, obj):
        """Método que retorna um status baseado na temperatura."""
        if obj.temperature < 0:
            return 'Frio'
        elif 0 <= obj.temperature < 20:
            return 'Ameno'
        elif 20 <= obj.temperature < 30:
            return 'Quente'
        else:
            return 'Muito Quente'

    temperature_status.short_description = 'Status da Temperatura'
