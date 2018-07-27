from django.shortcuts import render, get_object_or_404, redirect

from .models import Task


def add_view(request):
    if request.method == 'POST':
        try:
            task_id = int(request.POST.get('task', None))
        except:
            return redirect('task:home')
        if task_id == 0:
            task_new = Task.objects.create(
                type=1,
            )
        else:
            task = get_object_or_404(Task, id=task_id)
            task_new = Task.objects.create(
                type=1,
                name=task.name,
                code=task.code,
                text=task.text
            )
        return redirect('task:edit', task_new.id)
    task_list = Task.objects.filter(type=0)
    return render(
        request,
        'task/add.html',
        {
            'NAV': 'task',
            'task_list': task_list
        }
    )
