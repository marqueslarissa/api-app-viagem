# Generated by Django 3.0.7 on 2020-07-05 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='cliente',
        ),
    ]
