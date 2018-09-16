from django.db import models


class Config(models.Model):
    key = models.CharField(max_length=24, db_index=True)
    secret = models.CharField(max_length=255)

    def __str__(self):
        return self.key


class Version(models.Model):
    config = models.ForeignKey(Config, on_delete=models.CASCADE)

    revision = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    datetime_create = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-datetime_create']
