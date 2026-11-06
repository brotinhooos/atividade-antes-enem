from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CategoriaForm, TagForm
from .models import Categoria, Tag, Noticia


def home(request):
    return render(request, "noticias/home.html", {
        "categorias": Categoria.objects.all(),
        "tags": Tag.objects.all(),
        "noticias": Noticia.objects.select_related("categoria").prefetch_related("tags"),
    })


def categoria_lista(request):
    return render(request, "noticias/categoria_lista.html", {"categorias": Categoria.objects.all()})


def categoria_criar(request):
    form = CategoriaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Categoria cadastrada com sucesso!")
        return redirect("categoria_lista")
    return render(request, "noticias/form.html", {"form": form, "titulo": "Cadastrar categoria", "voltar": "categoria_lista"})


def categoria_editar(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Categoria atualizada com sucesso!")
        return redirect("categoria_lista")
    return render(request, "noticias/form.html", {"form": form, "titulo": "Atualizar categoria", "voltar": "categoria_lista"})


def categoria_excluir(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        try:
            categoria.delete()
            messages.success(request, "Categoria excluída com sucesso!")
        except ProtectedError:
            messages.error(request, "Não é possível excluir esta categoria, pois existem notícias vinculadas a ela.")
        return redirect("categoria_lista")
    return render(request, "noticias/confirmar_exclusao.html", {
        "objeto": categoria, "tipo": "categoria", "voltar": "categoria_lista"
    })


def tag_lista(request):
    return render(request, "noticias/tag_lista.html", {"tags": Tag.objects.all()})


def tag_criar(request):
    form = TagForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Tag cadastrada com sucesso!")
        return redirect("tag_lista")
    return render(request, "noticias/form.html", {"form": form, "titulo": "Cadastrar tag", "voltar": "tag_lista"})


def tag_editar(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    form = TagForm(request.POST or None, instance=tag)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Tag atualizada com sucesso!")
        return redirect("tag_lista")
    return render(request, "noticias/form.html", {"form": form, "titulo": "Atualizar tag", "voltar": "tag_lista"})


def tag_excluir(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        tag.delete()
        messages.success(request, "Tag excluída com sucesso!")
        return redirect("tag_lista")
    return render(request, "noticias/confirmar_exclusao.html", {
        "objeto": tag, "tipo": "tag", "voltar": "tag_lista"
    })
