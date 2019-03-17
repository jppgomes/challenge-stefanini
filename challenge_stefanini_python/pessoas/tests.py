import pytest
from django.shortcuts import reverse
# from django.contrib.auth.models import User
import json
import requests
# pytestmark = pytest.mark.django_db


URL_API = 'http://localhost:8000'

import pytest
from django.shortcuts import reverse
# from django.contrib.auth.models import User
import json
import requests
# pytestmark = pytest.mark.django_db


URL_API = 'http://localhost:8000'

def test_get_pessoas_return_200(client):
    
    url = URL_API+'/pessoas'
    response = requests.get(url)

    assert response.status_code == 200


def test_get_pessoa_return_200(client):
    url = URL_API+'/pessoas/1'
    
    response = requests.get(url)

    assert response.status_code == 200

def test_post_pessoa_return_201(client):

    url = URL_API+'/pessoas/'
    json =    {            
                    "nome": "jhon pedro",
                    "sobrenome": "Ferreira",
                    "cpf": "03231425166",
                    "email": "joaok8@gmail.com"
                }
    response = requests.post(url, json=json)

    assert response.status_code == 201

def test_put_pessoa_return_200(client):

    url = URL_API+'/pessoas/1/'
    
    json = {
    "id": 1,
    "nome": "jhon pedro",
    "sobrenome": "Ferreira",
    "cpf": "03231425166",
    "email": "joaok8@gmail.com"
    }
    
    response = requests.put(url, json=json)

    assert response.status_code == 200


def test_post_pessoa_return_500(client):

    url = URL_API+'/pessoas'
    json = {
            "id": 1,
            "nome": "Joao pedro",
            "sobrenome": "Ferreira",
            "cpf": "03231425166"        
        }
    response = requests.post(url, json=json)

    assert response.status_code == 500


def test_get_pessoas_return_404(client):
    
    url = URL_API+'/pessoa'
    response = requests.get(url)

    assert response.status_code == 404


def test_get_pessoa_return_404(client):
    url = URL_API+'/pessoa/1'
    
    response = requests.get(url)

    assert response.status_code == 404




