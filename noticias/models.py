from django.db import models

class Categoria(models.Model):
    nome = models.CharField("nome", max_length=100, unique=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField("nome", max_length=50, unique=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return self.nome


class Noticia(models.Model):
    titulo = models.CharField("título", max_length=180)
    conteudo = models.TextField("conteúdo")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="noticias",
        verbose_name="categoria"
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="noticias")

    class Meta:
        ordering = ["titulo"]
        verbose_name = "notícia"
        verbose_name_plural = "notícias"

    def __str__(self):
        return self.titulo
