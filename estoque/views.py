from django.http import Http404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,

)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

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
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer


class LoteDetail(RetrieveUpdateDestroyAPIView):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer


class LoteBusca(APIView):
    def get_object(self, nome):
        try:
            return Lote.objects.filter(nome__contains=nome)
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
    """
    codigo: '',
                nome_produto:'',
                tipo: '',
                data_fabricacao: '',
                validade: '',
                lotes: '',
                unidades: '',
                preco_unidade: ''
    """
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            preco_lote = data.preco_unidade * data.unidades
            produto = Produto(
                nome=data.nome_produto,
                preco=float(data.preco_unidade),
                codigo=data.codigo,
                tipo=int(data.tipo),
                fabricacao=data.data_fabricacao,
                validade=data.validade,
                unidades=int(data.unidades)
                )
            produto.save()
            lotes = []
            for lote in range(data.lotes):
                l = Lote(
                    codigo=data.codigo,
                    quantidade=int(data.unidades),
                    fabricacao=data.data_fabricacao,
                    validade=data.validade,
                    produto=int(produto.id),
                    preco=float(preco_lote)
                )
                lotes.append(l)
            Lote.objects.bulk_create(lotes)
            produto = ProdutoSerializer(data=produto)
            return Response(produto.data, status=status.HTTP_201_CREATED)
        except Exception:
            return self.create(request, *args, **kwargs)

class ProdutoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all().order_by('nome')
    serializer_class = ProdutoSerializer


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