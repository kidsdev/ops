from django.db import models


class Docker(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=120, db_index=True)

    sort = models.IntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['sort']


class Compose(models.Model):
    dockers = models.ManyToManyField(Docker)

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=120, db_index=True)

    sort = models.IntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['sort']
