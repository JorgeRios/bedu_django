from django.db import models

# Create your models here.

class Client(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.CharField(max_length=4)

    def __str__(self):
        return "{} {}".format(self.nombre, self.edad)
    
    def onlyName(self):
        return self.name


class Travel(models.Model):
    titulo = models.CharField(max_length=100)
    mes = models.CharField(max_length=4)
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
