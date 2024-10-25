from django.db import models

class Produto(models.Model):

# Create your models here.
    codigoProduto = models.Charfield(max_length=255)
    tituloProduto = models.Charfield(max_length=255)
    preco = models.Decimalfield(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=255)
    imagemProduto = models.Charfield(max_length=255)
    categoriaProduto = models.Charfield(max_length=255)
    classificacaoProduto = models.Decimalfield(max_digits=2, decimal_places=2)
    exibirHome = models.BooleanField(default=True)
