from rest_framework import viewsets, filters
from .serializers import *

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome',)