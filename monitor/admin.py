from django.contrib import admin

from .models import Monitor, Chart


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ('node', 'docker_compose', 'name', 'code', 'type', 'sort')


@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    list_display = ('monitor', 'chart')
