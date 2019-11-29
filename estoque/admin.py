from django.contrib import admin
from .models import (
    Produto,
    Lote,
    Tipo
)
# Register your models here.
admin.site.register(Lote)
admin.site.register(Produto)
admin.site.register(Tipo)