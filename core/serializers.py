from rest_framework import serializers
from .models import Cliente, Reserva, Hotel, Voo 

# Serializers define the API representation. Template.
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','primeiro_nome', 'ultimo_nome', 'endereco', 'telefone', 'celular', 'email', 'detalhes', 'data_cadastro']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'customer', 'cpf', 'data_compra', 'preco_total']

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'quarto', 'quantidade_adulto', 'quantidade_crianca', 'data_ida', 'data_volta', 'preco_unitario', 'preco_total',
                  'quantidade_estrela', 'cidade', 'distrito', 'nome_hotel', 'quantidade_quarto']

class VooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voo
        fields = ['id', 'preco_unitario', 'preco_total', 'direto', 'companhia_ida', 'origem_ida', 'origem_sigla_ida', 'destino_ida', 'destino_sigla_ida', 'data_ida',
                  'companhia_volta', 'origem_volta', 'origem_sigla_volta', 'destino_volta', 'destino_sigla_volta', 'data_volta', 'quantidade_passagem']
