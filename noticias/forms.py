from django import forms
from .models import Categoria, Tag

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome"]
        widgets = {"nome": forms.TextInput(attrs={"placeholder": "Nome da categoria"})}


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["nome"]
        widgets = {"nome": forms.TextInput(attrs={"placeholder": "Nome da tag"})}
