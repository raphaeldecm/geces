from django.urls import path

from . import views

app_name = 'movement'
urlpatterns = [
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('listar_produtos/', views.listar_produtos, name='listar_produtos'),
    path('editar_produto/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('excluir_produto/<int:pk>/', views.excluir_produto, name='excluir_produto'),
]
