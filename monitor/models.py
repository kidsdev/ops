from django.db import models


class Monitor(models.Model):
    TYPE_CHOICES = (
        (1, 'Stacked Area'),
    )

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=120, db_index=True)
    type = models.SmallIntegerField(choices=TYPE_CHOICES)

    sort = models.IntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['sort']
