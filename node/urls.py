from django.urls import path

from .views import home_view
from .views_detail import detail_view

app_name = 'node'
urlpatterns = [
    path('', home_view, name='home'),
    path('<int:node_id>/', detail_view, name='detail'),
]
