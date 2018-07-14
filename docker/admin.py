from django.contrib import admin

from .models import Docker, Compose


@admin.register(Docker)
class DockerAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'sort')


@admin.register(Compose)
class ComposeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'sort')
