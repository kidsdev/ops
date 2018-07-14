from django.shortcuts import render

from utils.decorators import permission_required
from .models import Server


@permission_required(['server.add_server', 'server.change_server', 'server.delete_server'], raise_exception=True)
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
