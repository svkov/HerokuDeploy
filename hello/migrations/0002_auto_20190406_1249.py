# Generated by Django 2.2 on 2019-04-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='something',
            name='name',
        ),
        migrations.AddField(
            model_name='something',
            name='text',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
