from django.db import models

class Cadastrados(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    nasc = models.CharField(max_length=20)
    idade = models.IntegerField()
    genero = models.CharField(max_length=50)
    naturalidade = models.CharField(max_length=50)
    tempo = models.IntegerField()
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=20)
    nis = models.CharField(max_length=20)
    sus = models.CharField(max_length=20)
    mae = models.CharField(max_length=255)
    pai = models.CharField(max_length=255)
    resp = models.CharField(max_length=255)
    parentesco = models.CharField(max_length=50)
    end = models.CharField(max_length=150)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    tel = models.IntegerField()
    cel = models.IntegerField()
    enc = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    

    def __str__(self):
        return f"Nome [nome={self.nome}]"