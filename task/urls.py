from django.urls import path

from .views import home_view
from .views_add import add_view
from .views_edit import edit_view

app_name = 'task'
urlpatterns = [
    path('', home_view, name='home'),
    path('add/', add_view, name='add'),
    path('<int:task_id>/edit/', edit_view, name='edit'),
]
