from django.db import models


class Chart(models.Model):
    TYPE_CHOICES = (
        (1, 'GAUGE'),
        (2, 'COUNTER'),
        (3, 'DERIVE'),
        (4, 'ABSOLUTE')
    )

    UNIT_CHOIECS = (
        (1, '%'),
        (10, 'KB'),
        (11, 'MB'),
        (20, 'req'),
        (21, 'req/s'),
        (30, 'Hour'),
        (31, 'Day')
    )

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=120, db_index=True)
    type = models.SmallIntegerField(choices=TYPE_CHOICES)
    unit = models.SmallIntegerField(choices=UNIT_CHOIECS)
    sort = models.IntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['sort']


class DateDay(models.Model):
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    max = models.FloatField()
    value = models.FloatField()
    min = models.FloatField()

    date = models.DateField(db_index=True)

    class Meta:
        ordering = ['date']

class DataHour(models.Model):
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    max = models.FloatField()
    value = models.FloatField()
    min = models.FloatField()

    date = models.DateField(db_index=True)
    hour = models.SmallIntegerField(db_index=True)

    class Meta:
        ordering = ['date', 'hour']
