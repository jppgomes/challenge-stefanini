from pessoas.models import Pessoa
from rest_framework import viewsets
from pessoas.serializers import PessoaSerializer
from enderecos.serializers import EnderecoSerializer
 


class PessoaViewSet(viewsets.ModelViewSet):

    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer