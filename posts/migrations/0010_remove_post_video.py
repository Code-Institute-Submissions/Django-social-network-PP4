# Generated by Django 3.2 on 2022-05-27 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20220524_0729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
    ]
