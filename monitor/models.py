from django.db import models


class Monitor(models.Model):
    TYPE_CHOICES = (
        (1, 'Stacked Area'),
    )

    node = models.ForeignKey('node.Node', null=True, on_delete=models.SET_NULL)
    docker_compose = models.ForeignKey('docker.Compose', null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=120, db_index=True)
    type = models.SmallIntegerField(choices=TYPE_CHOICES)

    sort = models.IntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['sort']

    def __str__(self):
        return self.name


class Chart(models.Model):
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    chart = models.ForeignKey('chart.Chart', on_delete=models.CASCADE)
