# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class CursoBorrar(models.Model):
    nombre=models.CharField(max_length=28)
    creditos=models.PositiveSmallIntegerField()
