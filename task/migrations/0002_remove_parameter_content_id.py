# Generated by Django 2.0.7 on 2018-07-16 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parameter',
            name='content_id',
        ),
    ]
