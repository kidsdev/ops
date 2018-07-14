from django.shortcuts import render

from server.models import Server
from utils.decorators import permission_required
from utils.paginator import listing, get_q
from .models import Node


@permission_required(['node.add_node', 'node.change_node', 'node.delete_node'], raise_exception=True)
def home_view(request):
    node_list = Node.objects.select_related('server').all()
    try:
        q_server = int(request.GET.get('q_server', None))
    except:
        q_server = None

    if q_server and q_server > 0:
        try:
            q_server = int(q_server)
            node_list = node_list.filter(server_id=q_server)
        except:
            pass

    node_list = listing(request, node_list)
    server_list = Server.objects.all()

    return render(
        request,
        'node/home.html',
        {
            'NAV': 'node',
            'node_list': node_list,
            'server_list': server_list,
            'q_server': q_server,
            'q_paginator': get_q({
                'q_server': q_server
            })
        }
    )
