# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from enderecos.serializers import EnderecoSerializer
from rest_framework import viewsets
from enderecos.models import Endereco


# Create your views here.


class EnderecoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows enderecos to be viewed or edited.
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
