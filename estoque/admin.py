from django.contrib import admin
from .models import Produto, Lote
# Register your models here.
admin.site.register(Lote)
admin.site.register(Produto)