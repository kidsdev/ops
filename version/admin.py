from django.contrib import admin

from .models import Config, Version


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('key',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('config', 'revision', 'value', 'datetime_create')
