from rest_framework.serializers import ModelSerializer
from .models import *


class LoteSerializer(ModelSerializer):
    class Meta:
        model = Lote
        fields = '__all__'


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
