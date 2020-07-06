# Generated by Django 3.0.7 on 2020-07-06 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='cpf',
        ),
        migrations.AddField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(default='11111111111', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='cliente',
            constraint=models.UniqueConstraint(fields=('id', 'cpf'), name='cliente_cpf_constraint'),
        ),
    ]
