from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField
)
from .models import *


class LoteSerializer(ModelSerializer):

    class Meta:
        model = Lote
        fields = '__all__'


class ProdutoSerializer(ModelSerializer):
    lotes = PrimaryKeyRelatedField(many=True, queryset=Lote.objects.all())
    class Meta:
        model = Produto
        fields = '__all__'
