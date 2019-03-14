# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinLengthValidator
# from enderecos.models import Endereco


class Pessoa(models.Model):
    
    nome = models.CharField(max_length=50, blank=False, verbose_name="Nome")
    sobrenome = models.CharField(max_length=50, blank=False, verbose_name="Sobrenome")
    cpf = models.CharField(max_length=11, blank=False, verbose_name="Cpf")
    email = models.CharField(max_length=20, blank=False, verbose_name="Email")
