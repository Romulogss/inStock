from django.db import models


# Create your models here.

class Tipo(models.Model):
    nome = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(
        max_length=100
    )
    preco = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    codigo = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )
    tipo = models.ForeignKey(
        Tipo,
        models.DO_NOTHING,
        related_name='produtos'
    )
    fabricacao = models.DateField()
    validade = models.DateField()
    unidades = models.IntegerField()

    def __str__(self):
        return self.nome



class Lote(models.Model):
    quantidade = models.IntegerField(
        null=True,
        blank=True,
        default=0
    )
    codigo = models.CharField(
        max_length=10,
    )
    fabricacao = models.DateField()
    validade = models.DateField()
    entrada = models.DateField()
    produto = models.ForeignKey(
        Produto,
        models.DO_NOTHING,
        related_name='lotes'
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.codigo
