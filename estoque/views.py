from django.http import Http404, HttpResponse
from django.shortcuts import render
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
    Produto,
    Tipo
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
            return Lote.objects.filter(nome__icontains=nome)
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
    Ao adicionar um lote alocamos os dados em seus devidos lugares apropriados
    """

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            preco_lote = float(data['preco_unidade']) * int(data['unidades'])
            tipo = Tipo.objects.get(pk=int(data['tipo']))
            produto = Produto(
                nome=data['nome_produto'],
                preco=float(data['preco_unidade']),
                codigo=data['codigo'],
                tipo=tipo,
                fabricacao=data['data_fabricacao'],
                validade=data['validade'],
                unidades=int(data['unidades'])
            )
            produto.save()
            lotes = []
            for lote in range(int(data['lotes'])):
                l = Lote(
                    codigo=data['codigo'],
                    quantidade=int(data['unidades']),
                    fabricacao=data['data_fabricacao'],
                    validade=data['validade'],
                    produto=produto,
                    preco=float(preco_lote)
                )
                lotes.append(l)
            Lote.objects.bulk_create(lotes)
            produto = ProdutoSerializer(produto)
            return Response(produto.data, status=status.HTTP_201_CREATED)
        except Exception:
            print()
            return self.create(request, *args, **kwargs)


class ProdutoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all().order_by('nome')
    serializer_class = ProdutoSerializer


class ProdutoBusca(APIView):

    def get_object(self, nome):
        try:
            return Produto.objects.filter(nome__icontains=nome)
        except Produto.DoesNotExist:
            raise Http404

    def get(self, request, nome):
        produtos = self.get_object(nome)
        produtos_s = ProdutoSerializer(produtos, many=True)
        return Response(produtos_s.data)
