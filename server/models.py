from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=120, db_index=True)

    user = models.CharField(max_length=24)
    ip = models.CharField(max_length=24)
    sort = models.IntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['sort']
