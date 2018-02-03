from django.contrib import admin

from .models import Node


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('server', 'docker_compose', 'name', 'code', 'path', 'sort')
