# Generated by Django 5.1.2 on 2024-10-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cedula',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='edad',
            field=models.IntegerField(null=True),
        ),
    ]
