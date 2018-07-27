from django.contrib import admin

from .models import Task, History, Parameter, Log


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'code', 'datetime_update')


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('task', 'datetime_create')


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('task', 'content_type', 'field', 'sort')


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('task', 'status', 'datetime_create')
