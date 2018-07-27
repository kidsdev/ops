from django.shortcuts import render

from utils.decorators import permission_required
from .models import Task


@permission_required(['task.add_task', 'task.change_task', 'task.delete_task'], raise_exception=True)
def home_view(request):
    task_list = Task.objects.filter(type=1)
    return render(
        request,
        'task/home.html',
        {
            'NAV': 'task',
            'task_list': task_list,
        }
    )
