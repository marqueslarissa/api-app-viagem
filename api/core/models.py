from django.db import models


class Voo(models.Model):
    id = models.CharField(max_length=256, primary_key=True)
    precoUnit = models.CharField(max_length=256)
    precoTotal = models.CharField(max_length=256)
    direto = models.CharField(max_length=256)
    companhiaIda = models.CharField(max_length=256)
    origemIda = models.CharField(max_length=256)
    origemSiglaIda = models.CharField(max_length=256)
    destinoIda = models.CharField(max_length=256)
    destinoSiglaIda = models.CharField(max_length=256)
    dataIda = models.CharField(max_length=256)
    companhiaVolta = models.CharField(max_length=256)
    origemVolta = models.CharField(max_length=256)
    origemSiglaVolta = models.CharField(max_length=256)
    destinoVolta = models.CharField(max_length=256)
    destinoSiglaVolta = models.CharField(max_length=256)
    dataVolta = models.CharField(max_length=256)
    qtd = models.IntegerField()
    # 1 = voo, 2 = hotel
    tipo = 1
    storageKey = models.CharField(max_length=256)

    def __class__ (self):
        return self