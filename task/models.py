from django.db import models


class Task(models.Model):
    TYPE_CHOICES = (
        (0, 'Template'),
        (1, 'Task'),
    )

    type = models.SmallIntegerField(choices=TYPE_CHOICES, default=0)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, db_index=True)

    text = models.TextField()

    datetime_update = models.DateTimeField(auto_now=True, db_index=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime_update']

    def __str__(self):
        return self.code


class History(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    text = models.TextField()
    datetime_create = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-datetime_create']


class Parameter(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    content_type = models.ForeignKey('contenttypes.ContentType', on_delete=models.CASCADE)
    content_id = models.IntegerField()
    field = models.CharField(max_length=255)

    sort = models.SmallIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['sort']


class Log(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    args = models.TextField()
    result = models.TextField()
    status = models.CharField(max_length=255)

    datetime_create = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-datetime_create']
