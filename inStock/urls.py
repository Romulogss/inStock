"""inStock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from inStock import settings
from django.contrib import admin
from django.urls import path, include
from estoque.views import (
    LoteList,
    LoteDetail,
    ProdutoList,
    ProdutoDetail,
    ProdutoBusca,
    LoteBusca
)

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('lote', LoteListCreateView.as_view())

urlpatterns = [
    path('lote/', LoteList.as_view()),  # para acessar http://127.0.0.1:8000/lote/
    path('lote/<int:pk>', LoteDetail.as_view()),  # para acessar http://127.0.0.1:8000/lote/<id>
    path('lote/<str:nome>', LoteBusca.as_view()), # para acessar http://127.0.0.1:8000/lote/<nome>
    path('produto/', ProdutoList.as_view()),  # para acessar http://127.0.0.1:8000/produto/
    path('produto/<int:pk>', ProdutoDetail.as_view()),  # para acessar http://127.0.0.1:8000/produto/id
    path('produto/<str:nome>', ProdutoBusca.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),

                      # For django versions before 2.0:
                      # url(r'^__debug__/', include(debug_toolbar.urls)),

                  ] + urlpatterns
