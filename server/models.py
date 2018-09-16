from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=120, db_index=True)
    image = models.ImageField(upload_to='server/%Y/%m/', null=True, blank=True)

    user = models.CharField(max_length=24)
    ip = models.CharField(max_length=24)
    sort = models.IntegerField(default=0, db_index=True)

    datetime_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sort']

    def __str__(self):
        return self.name

    def get_node_count_live(self):
        return self.node_set.filter(status=2).count()
