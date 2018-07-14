from django.db import models


class Node(models.Model):
    STATUS_CHOICES = (
        (-3, 'Deleted'),
        (-2, 'Waiting Delete'),
        (-1, 'Pause'),
        (0, 'Waiting'),
        (1, 'Pending'),
        (2, 'Live'),
    )

    server = models.ForeignKey('server.Server', null=True, on_delete=models.SET_NULL)
    docker_compose = models.ForeignKey('docker.Compose', null=True, blank=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=120, db_index=True)
    url = models.CharField(max_length=255)

    path = models.CharField(max_length=255)
    port = models.CharField(max_length=120)
    tag = models.CharField(max_length=255)

    sort = models.IntegerField(default=0, db_index=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=0)

    datetime_update = models.DateTimeField(auto_now=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sort']

    def __str__(self):
        return self.name


class Log(models.Model):
    TYPE_CHOICES = (
        (1, 'develop'),
        (2, 'business'),
    )

    STATUS_CHOICES = (
        (-1, 'Failed'),
        (0, 'Waiting'),
        (1, 'Running'),
        (2, 'Completed'),
    )

    node = models.ForeignKey(Node, on_delete=models.CASCADE)

    type = models.SmallIntegerField(choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    message = models.TextField()
    status = models.SmallIntegerField(choices=STATUS_CHOICES)

    datetime_create = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-datetime_create']
