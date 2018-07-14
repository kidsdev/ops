from django.shortcuts import render

from utils.paginator import listing
from .models import Node


def home_view(request):
    node_list = Node.objects.select_related('server').all()
    node_list = listing(request, node_list)
    return render(
        request,
        'node/home.html',
        {
            'NAV': 'node',
            'node_list': node_list,
        }
    )
