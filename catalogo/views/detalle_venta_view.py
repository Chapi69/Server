from ..models_raiz import Detalle_venta
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class Detalle_ventaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detalle_venta
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')


class Detalle_ventaViewSet(viewsets.ModelViewSet):
    queryset = Detalle_venta.objects.all()
    serializer_class = Detalle_ventaSerializer
    
