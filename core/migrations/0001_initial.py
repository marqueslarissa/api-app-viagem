# Generated by Django 3.0.7 on 2020-07-06 04:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=64)),
                ('ultimo_nome', models.CharField(max_length=64)),
                ('endereco', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=32)),
                ('celular', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('detalhes', models.TextField(max_length=255)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarto', models.CharField(max_length=255)),
                ('quantidade_adulto', models.CharField(max_length=255)),
                ('quantidade_crianca', models.CharField(max_length=255)),
                ('data_ida', models.CharField(max_length=255)),
                ('data_volta', models.CharField(max_length=255)),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preco_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade_estrela', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('distrito', models.CharField(max_length=5)),
                ('nome_hotel', models.CharField(max_length=255)),
                ('quantidade_quarto', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Voo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preco_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('direto', models.CharField(max_length=255)),
                ('companhia_ida', models.CharField(max_length=255)),
                ('origem_ida', models.CharField(max_length=255)),
                ('origem_sigla_ida', models.CharField(max_length=5)),
                ('destino_ida', models.CharField(max_length=255)),
                ('destino_sigla_ida', models.CharField(max_length=5)),
                ('data_ida', models.CharField(max_length=255)),
                ('companhia_volta', models.CharField(max_length=255)),
                ('origem_volta', models.CharField(max_length=255)),
                ('origem_sigla_volta', models.CharField(max_length=5)),
                ('destino_volta', models.CharField(max_length=255)),
                ('destino_sigla_volta', models.CharField(max_length=5)),
                ('data_volta', models.CharField(max_length=255)),
                ('quantidade_passagem', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=20)),
                ('data_compra', models.DateField(auto_now_add=True)),
                ('preco_total', models.CharField(max_length=32)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='customer')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AddConstraint(
            model_name='reserva',
            constraint=models.UniqueConstraint(fields=('id', 'customer'), name='reserva_cliente_constraint'),
        ),
    ]
