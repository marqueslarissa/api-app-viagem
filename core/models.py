from django.db import models
import uuid
class Cliente(models.Model):
    id_cliente = models.UUIDField(default=uuid.uuid4, primary_key=True)
    primeiro_nome = models.CharField(max_length=64)
    ultimo_nome = models.CharField(max_length=64)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=32)
    celular = models.CharField(max_length=32)
    email = models.EmailField()
    detalhes = models.TextField(max_length=255)
    data_cadastro = models.DateField(auto_now_add=True)

class Reserva(models.Model):
    id_reserva = models.UUIDField(default=uuid.uuid4, primary_key=True)
    data_compra = models.DateField(auto_now_add=True)
    preco_total = models.CharField(max_length=32)
    data_pagamento = models.DateField(auto_now_add=True)

    def __class__ (self):
        return self

class Hotel(models.Model):
    id_quarto = models.UUIDField(default=uuid.uuid4, primary_key=True)
    quarto = models.CharField(max_length=255)
    quantidade_adulto = models.CharField(max_length=255)
    quantidade_crianca = models.CharField(max_length=255)
    data_ida = models.CharField(max_length=255)
    data_volta = models.CharField(max_length=255)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estrela = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    distrito = models.CharField(max_length=5)
    nome_hotel = models.CharField(max_length=255)
    quantidade_quarto = models.CharField(max_length=255)
    # 1 = voo, 2 = hotel
    tipo = 2

    def __class__ (self):
        return self

class Voo(models.Model):
    id_voo = models.UUIDField(default=uuid.uuid4, primary_key=True)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    direto = models.CharField(max_length=255)
    companhia_ida = models.CharField(max_length=255)
    origem_ida = models.CharField(max_length=255)
    origem_sigla_ida = models.CharField(max_length=5)
    destino_ida = models.CharField(max_length=255)
    destino_sigla_ida = models.CharField(max_length=5)
    data_ida = models.CharField(max_length=255)
    companhia_volta = models.CharField(max_length=255)
    origem_volta = models.CharField(max_length=255)
    origem_sigla_volta = models.CharField(max_length=5)
    destino_volta = models.CharField(max_length=255)
    destino_sigla_volta = models.CharField(max_length=5)
    data_volta = models.CharField(max_length=255)
    quantidade_passagem = models.IntegerField()
    # 1 = voo, 2 = hotel
    tipo = 1

    def __class__ (self):
        return self