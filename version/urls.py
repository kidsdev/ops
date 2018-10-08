from django.urls import path

from .views_increment import increment_view
from .views_last import last_view

app_name = 'version'
urlpatterns = [
    path('increment/', increment_view),
    path('last/', last_view),
]
