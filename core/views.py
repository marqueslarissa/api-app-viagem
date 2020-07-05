from django.shortcuts import render
from rest_framework import viewsets, status

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_auth.views import LogoutView
from .models import Cliente, Reserva, Hotel, Voo
from .serializers import ClienteSerializer, ReservaSerializer, HotelSerializer, VooSerializer

#ViewSets define the view behavior.
class TestAuthView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response("Hello {0}!".format(request.user))

class LogoutViewEx(LogoutView):
    authentication_classes = (TokenAuthentication,)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    @csrf_exempt
    def list(self, request):
        """
        Lista todos os clientes, ou cria um novo cliente.
        """
        if request.method == 'GET':
            clientes = Cliente.objects.all()
            serializer = ClienteSerializer(clientes, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
           # data = JSONParser().parse(request)
            serializer = ClienteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

    @csrf_exempt
    def detail(self, request, pk):
        """
        Retrieve, update or delete um cliente.
        """ 
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response(status=404)

        if request.method == 'GET':
            serializer = ClienteSerializer(cliente)
            return Response(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ClienteSerializer(cliente, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

        elif request.method == 'DELETE':
            cliente.delete()
            return Response(status=204)

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    @csrf_exempt
    def list(request):
        """
        Lista todas as reservas, ou cria uma nova reserva.
        """
        if request.method == 'GET':
            reservas = Reserva.objects.all()
            serializer = ReservaSerializer(reservas, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
           # data = JSONParser().parse(request)
            serializer = ReservaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

    @csrf_exempt
    def detail(request, pk):
        """
        Retrieve, update or delete uma reserva.
        """ 
        try:
            reserva = Reserva.objects.get(pk=pk)
        except Reserva.DoesNotExist:
            return Response(status=404)

        if request.method == 'GET':
            serializer = ReservaSerializer(reserva)
            return Response(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ReservaSerializer(reserva, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

        elif request.method == 'DELETE':
            reserva.delete()
            return Response(status=204)

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    @csrf_exempt
    def list(self, request):
        """
        Lista todos os hoteis, ou cria um novo hotel.
        """
        if request.method == 'GET':
            hoteis = Hotel.objects.all()
            serializer = HotelSerializer(hoteis, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
           # data = JSONParser().parse(request)
            serializer = HotelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

    @csrf_exempt
    def detail(self, request, pk):
        """
        Retrieve, update or delete um hotel.
        """ 
        try:
            hotel = Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            return Response(status=404)

        if request.method == 'GET':
            serializer = HotelSerializer(hotel)
            return Response(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = HotelSerializer(hotel, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

        elif request.method == 'DELETE':
            hotel.delete()
            return Response(status=204)

class VooViewSet(viewsets.ModelViewSet):
    queryset = Voo.objects.all()
    serializer_class = VooSerializer

    @csrf_exempt
    def list(self, request):
        """
        Lista todos os voos, ou cria um novo voo.
        """
        if request.method == 'GET':
            voos = Voo.objects.all()
            serializer = VooSerializer(voos, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
           # data = JSONParser().parse(request)
            serializer = VooSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

    @csrf_exempt
    def detail(self, request, pk):
        """
        Retrieve, update or delete um voo.
        """ 
        try:
            voo = Voo.objects.get(pk=pk)
        except Voo.DoesNotExist:
            return Response(status=404)

        if request.method == 'GET':
            serializer = VooSerializer(voo)
            return Response(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = VooSerializer(voo, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

        elif request.method == 'DELETE':
            voo.delete()
            return Response(status=204)