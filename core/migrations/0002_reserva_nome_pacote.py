# Generated by Django 3.0.7 on 2020-07-05 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='nome_pacote',
            field=models.CharField(default='Reserva', max_length=255),
            preserve_default=False,
        ),
    ]
