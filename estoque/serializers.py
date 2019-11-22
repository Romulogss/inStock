from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField
)
from .models import *


class LoteSerializer(ModelSerializer):
    produtos = PrimaryKeyRelatedField(many=True, queryset=Produto.objects.all())
    class Meta:
        model = Lote
        fields = '__all__'


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
