import os

from django.conf import settings
from django.core.management.base import BaseCommand
from task.models import Task, Parameter


class Command(BaseCommand):
    help = 'Init Task Template.'

    def handle(self, *args, **options):
        count = 0
        path = os.path.join(settings.BASE_DIR, 'task', 'templates_fabric')

        for f in os.listdir(path):
            template = os.path.join(path, f)
            if os.path.isfile(template):
                count += 1
                code = f.replace('.txt', '')
                task = Task.objects.filter(type=0, code=code).first()
                if task is None:
                    task = Task(type=0, code=code)
                data = open(template, 'r').read().split('***')
                task.name = code.replace('_', ' ').title()
                task.text = data[1].strip()
                task.save()
                parameter_list = list(task.parameter_set.all())
                sort = 0
                for line in data[0].strip().split('\n'):
                    sort += 1
                    p = line.split(',')
                    content_type = settings.CONTENT_TYPE(p[0].strip())
                    field = p[1].strip()
                    try:
                        parameter = parameter_list.pop(0)
                        parameter.content_type = content_type
                        parameter.field = field
                        parameter.sort = sort
                        parameter.save()
                    except:
                        Parameter.objects.create(
                            task=task,
                            content_type=content_type,
                            field=field,
                            sort=sort
                        )

        self.stdout.write(self.style.SUCCESS('Successfully init %s tasks' % count))
