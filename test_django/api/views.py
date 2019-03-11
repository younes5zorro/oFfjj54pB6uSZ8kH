from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import Connection
from api.serializers import ConnectionSerializer


class ConnectionCreateView(ListCreateAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer

class ConnectionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer