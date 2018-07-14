from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import home_view
from .views_login import login_view
from .views_logout import logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),

    path('server/', include('server.urls')),
    path('node/', include('node.urls')),

    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
