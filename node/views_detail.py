from django.conf import settings
from django.shortcuts import render, get_object_or_404

from task.models import Task
from utils.decorators import permission_required
from utils.paginator import listing
from .models import Node


@permission_required(['node.change_node'], raise_exception=True)
def detail_view(request, node_id):
    node = get_object_or_404(Node, id=node_id)
    task_list = Task.objects.filter(parameter__content_type=settings.CONTENT_TYPE('node.node')).distinct()
    log_list = node.log_set.all()
    log_list = listing(request, log_list)
    return render(
        request,
        'node/detail.html',
        {
            'NAV': 'node',
            'node': node,
            'task_list': task_list,
            'log_list': log_list
        }
    )
