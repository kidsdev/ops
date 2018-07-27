from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings

from .forms import TaskForm
from .models import Task
import os


def edit_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            path = os.path.join(settings.BASE_DIR, 'task', 'tasks', '%s.py' % task.code)
            data = """from fabric import Connection
from invoke import task

@task
def deploy(c):
"""
            for line in task.text.split('\n'):
                data += '    %s\n' % line.strip()
            with open(path, 'w') as f:
                f.write(data)
            return redirect('task:home')
    else:
        form = TaskForm(instance=task)
    return render(
        request,
        'task/edit.html',
        {
            'NAV': 'task',
            'form': form
        }
    )
