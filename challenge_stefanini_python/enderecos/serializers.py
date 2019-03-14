# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from enderecos.models import Endereco


# Serializer do endereço, utilizando hiperlinked model
class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id',  'logradouro', 'bairro', 'cidade', 'uf', 'pessoa')
