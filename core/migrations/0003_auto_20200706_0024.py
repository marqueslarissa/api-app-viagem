# Generated by Django 3.0.7 on 2020-07-06 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_reserva_data_pagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='itens_pacote',
            field=models.IntegerField(),
        ),
    ]
