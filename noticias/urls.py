from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("categorias/", views.categoria_lista, name="categoria_lista"),
    path("categorias/nova/", views.categoria_criar, name="categoria_criar"),
    path("categorias/<int:pk>/editar/", views.categoria_editar, name="categoria_editar"),
    path("categorias/<int:pk>/excluir/", views.categoria_excluir, name="categoria_excluir"),
    path("tags/", views.tag_lista, name="tag_lista"),
    path("tags/nova/", views.tag_criar, name="tag_criar"),
    path("tags/<int:pk>/editar/", views.tag_editar, name="tag_editar"),
    path("tags/<int:pk>/excluir/", views.tag_excluir, name="tag_excluir"),
]
