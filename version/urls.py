from django.urls import path


from .views_increment import increment_view

app_name = 'version'
urlpatterns = [
    path('increment/', increment_view),
]
