from django.contrib import admin

from .models import Chart, Day, Hour, Raw


@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    list_display = ('server', 'docker', 'node', 'name', 'code', 'type', 'unit', 'sort')


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('chart', 'max', 'value', 'min', 'date')


@admin.register(Hour)
class HourAdmin(admin.ModelAdmin):
    list_display = ('chart', 'max', 'value', 'min', 'date', 'hour')


@admin.register(Raw)
class RawAdmin(admin.ModelAdmin):
    list_display = ('chart', 'value', 'timestamp')
