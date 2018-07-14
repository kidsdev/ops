from django.db import models


class Chart(models.Model):
    TYPE_CHOICES = (
        (1, 'GAUGE'),
        (2, 'COUNTER'),
        (3, 'DERIVE'),
        (4, 'ABSOLUTE')
    )

    UNIT_CHOICES = (
        (1, '%'),
        (10, 'KB'),
        (11, 'MB'),
        (20, 'req'),
        (21, 'req/s'),
        (30, 'Hour'),
        (31, 'Day')
    )

    server = models.ForeignKey('server.Server', null=True, on_delete=models.SET_NULL)
    docker = models.ForeignKey('docker.Docker', null=True, on_delete=models.SET_NULL)
    node = models.ForeignKey('node.Node', null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=120, db_index=True)
    type = models.SmallIntegerField(choices=TYPE_CHOICES)
    unit = models.SmallIntegerField(choices=UNIT_CHOICES)
    sort = models.IntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['sort']

    def __str__(self):
        return self.name


class Day(models.Model):
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    max = models.FloatField()
    value = models.FloatField()
    min = models.FloatField()

    date = models.DateField(db_index=True)

    class Meta:
        ordering = ['date']


class Hour(models.Model):
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    max = models.FloatField()
    value = models.FloatField()
    min = models.FloatField()

    date = models.DateField(db_index=True)
    hour = models.SmallIntegerField(db_index=True)

    class Meta:
        ordering = ['date', 'hour']


class Raw(models.Model):
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    value = models.FloatField()
    timestamp = models.DateTimeField(db_index=True)

    class Meta:
        ordering = ['-timestamp']
