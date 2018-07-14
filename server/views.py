from django.shortcuts import render

from .models import Server


def home_view(request):
    server_list = Server.objects.all()
    return render(
        request,
        'server/home.html',
        {
            'NAV': 'server',
            'server_list': server_list,
        }
    )
