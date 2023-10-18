from django.urls import path

from . import views

app_name = 'movement'
urlpatterns = [
    path('cadastrar_produto', views.cadastrar_produto, name='cadastrar_produto'),
]
