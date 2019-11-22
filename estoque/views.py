from django.http import Http404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,

)
from rest_framework.response import Response
from rest_framework.views import APIView

from django_filters import rest_framework as filters
from .serializers import (
    ProdutoSerializer,
    LoteSerializer
)
from .models import (
    Lote,
    Produto
)
# Create your views here.


class LoteList(ListCreateAPIView):
    queryset = Lote.objects.all().order_by('nome_produto')
    serializer_class = LoteSerializer


class LoteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer


class LoteBusca(APIView):
    def get_object(self, nome):
        try:
            return Lote.objects.filter(nome_produto__contains=nome)
        except Lote.DoesNotExist:
            raise Http404

    def get(self, request, nome):
        lotes = self.get_object(nome)
        lotes_s = LoteSerializer(lotes, many=True)
        return Response(lotes_s.data)


class ProdutoList(ListCreateAPIView):
    queryset = Produto.objects.all().order_by('nome')
    serializer_class = ProdutoSerializer

    """
    sobescrevendo o método POST para adicionar lógica de quantidade de produto
    no lote
    """

    def post(self, request, *args, **kwargs):
        produto = request.data
        lote = Lote.objects.get(pk=int(produto['lote']))
        if lote.quantidade is not None:
            lote.quantidade += 1
        else:
            lote.quantidade = 1
        lote.save()
        return self.create(request, *args, **kwargs)


class ProdutoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all().order_by('nome')
    serializer_class = ProdutoSerializer

    def delete(self, request, *args, **kwargs):
        produto = kwargs.get('pk')
        produto = Produto.objects.get(pk=produto)
        lote = produto.lote
        lote.quantidade -= 1
        lote.save()
        return self.destroy(request, *args, **kwargs)


class ProdutoBusca(APIView):

    def get_object(self, nome):
        try:
            return Produto.objects.filter(nome__contains=nome)
        except Produto.DoesNotExist:
            raise Http404

    def get(self, request, nome):
        produtos = self.get_object(nome)
        produtos_s = ProdutoSerializer(produtos, many=True)
        return Response(produtos_s.data)
