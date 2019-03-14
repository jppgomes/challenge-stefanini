# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinLengthValidator
from pessoas.models import Pessoa


class Endereco(models.Model):
    
    logradouro = models.CharField(max_length=50, blank=False, verbose_name="Logradouro")
    bairro = models.CharField(max_length=50, blank=False, verbose_name="Bairro")
    cidade = models.CharField(max_length=20, blank=False, verbose_name="Cidade")
    uf = models.CharField(max_length=2, blank=False, verbose_name="UF")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)