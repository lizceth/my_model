from __future__ import unicode_literals

from django.db import models

class Categoria (models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre
