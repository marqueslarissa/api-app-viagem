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
        List all clients, or create a new client.
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
        Retrieve, update or delete a client.
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

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class VooViewSet(viewsets.ModelViewSet):
    queryset = Voo.objects.all()
    serializer_class = VooSerializer
