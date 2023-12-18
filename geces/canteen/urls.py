from django.urls import path

from . import views

app_name = "canteen"
urlpatterns = [
    path("cadastrar_produto/", views.ProductFormView.as_view(), name="product_form"),
    path("listar_produtos/", views.ProductListView.as_view(), name="product_list"),
    path("editar_produto/<int:pk>/", views.ProductUpdateView.as_view(), name="product_update"),
    path("excluir_produto/<int:pk>/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("visualizar_produto/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
]
