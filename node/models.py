from django.db import models


class Node(models.Model):
    server = models.ForeignKey('server.Server', null=True, on_delete=models.SET_NULL)
    docker_compose = models.ForeignKey('docker.Compose', null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=120, db_index=True)
    path = models.CharField(max_length=255)

    sort = models.IntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['sort']

    def __str__(self):
        return self.name
