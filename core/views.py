from django.shortcuts import render
from rest_framework import viewsets

from .models import Voo
from .serializers import VooSerializer

# ViewSets define the view behavior.
class VooViewSet(viewsets.ModelViewSet):
    queryset = Voo.objects.all()
    serializer_class = VooSerializer
