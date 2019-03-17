# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from enderecos.models import Endereco
from pessoas.models import Pessoa

# Serializer do usuário, utilizando hiper linked model
class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id', 'nome', 'sobrenome', 'cpf', 'email')

    
        def __unicode__(self):
            return '%s' % self.nome