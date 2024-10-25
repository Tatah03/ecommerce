from django.db import models

class Produto(models.Model):

# Create your models here.
    tituloProduto = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=255)
    imagemProduto = models.CharField(max_length=255)
    categoriaProduto = models.CharField(max_length=255)
    classificacaoProduto = models.DecimalField(max_digits=2, decimal_places=2)
    exibirHome = models.BooleanField(default=True)
