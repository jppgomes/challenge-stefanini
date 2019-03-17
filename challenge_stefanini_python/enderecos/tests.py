import pytest
from django.shortcuts import reverse
# from django.contrib.auth.models import User
import json
import requests
# pytestmark = pytest.mark.django_db


URL_API = 'http://localhost:8000'

def test_get_enderecos_return_200(client):
    
    url = URL_API+'/enderecos'
    response = requests.get(url)

    assert response.status_code == 200


def test_get_endereco_return_200(client):
    url = URL_API+'/enderecos/1'
    
    response = requests.get(url)

    assert response.status_code == 200

def test_post_endereco_return_201(client):

    url = URL_API+'/enderecos/'
    json =    {            
                    "logradouro": "teste",
                    "bairro": "teste",
                    "cidade": "teste",
                    "uf": "uf",
                    "pessoa": URL_API+"/pessoas/1/"
                }
    response = requests.post(url, json=json)

    assert response.status_code == 201

def test_put_endereco_return_200(client):

    url = URL_API+'/enderecos/1/'
    
    json =    {            
                    "id": 1,
                    "logradouro": "teste2",
                    "bairro": "teste2",
                    "cidade": "teste2",
                    "uf": "uf",
                    "pessoa": URL_API+"/pessoas/1/"
                }

    response = requests.put(url, json=json)

    assert response.status_code == 200


def test_post_endereco_return_500(client):

    url = URL_API+'/enderecos'
    json = {
            "id": 1,
            "nome": "Joao pedro",
            "sobrenome": "Ferreira",
            "cpf": "03231425166"        
        }
    response = requests.post(url, json=json)

    assert response.status_code == 500


def test_get_endereco_return_404(client):
    
    url = URL_API+'/endereco'
    response = requests.get(url)

    assert response.status_code == 404


def test_get_endereco_return_404(client):
    url = URL_API+'/endereco/1'
    
    response = requests.get(url)

    assert response.status_code == 404




