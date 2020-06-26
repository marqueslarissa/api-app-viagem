from rest_framework import serializers
from .models import Voo

# Serializers define the API representation. Template.


class VooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voo
        fields = ['precoUnit', 'precoTotal', 'direto', 'companhiaIda', 'origemIda', 'origemSiglaIda', 'destinoIda', 'destinoSiglaIda', 'dataIda',
                  'companhiaVolta', 'origemVolta', 'origemSiglaVolta', 'destinoVolta', 'destinoSiglaVolta', 'dataVolta', 'qtd', 'tipo']
