from django.db import models

class Piloto(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Moto(models.Model):
    modelo = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    cilindrada = models.IntegerField()  # Cilindrada em cc
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.marca} {self.modelo}'

class Corrida(models.Model):
    data_corrida = models.DateField()
    localizacao = models.CharField(max_length=200)
    motos_participantes = models.ManyToManyField(Moto)

    def __str__(self):
        return f'Corrida em {self.localizacao} na data {self.data_corrida}'