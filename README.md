# Desafio realizado para seleção na Stefanini

# Instalação
## Passo 1: Dentro da pasta challenge-stefanini, rodar `utils.sh` com o seguinte comando `source ./utils.sh`, script inicializa a virtual-env. 

## Passo 2: Rodar o container do postgres, `sudo docker-compose up -d`

## Passo 3: Checar mudanças de migração para o banco `python3 manage.py makemigrations`

## Passo 4: Aplicar migração `python3 manage.py migrate`

## Passo 5: Iniciar a aplicação com `python3 manage.py runserver`

## Passo 6: Rodar os testes unitários `pytest` (Na mesma pasta do arquivo manage.py)

# API Documentation for challenge.

## `GET /pessoas/`

Retorna todas as pessoas, no precisa de autenticação

## `POST /pessoas/`

Cria uma nova pessoa

## `DELETE /pessoas/{id}`

Cria uma nova pessoa

##### PARAMS:

*  **`Nome`** nome da pessoa

*  **`Sobrenome`** Sobrenome da pessoa.

*  **`Cpf`** CPf da pessoa, deve conter 11 caracteres.

*  **`Email`** Email da pessoa.


## `PUT /pessoas/{id}`

Atualiza uma nova pessoa

##### PARAMS:

*  **`Nome`** nome da pessoa

*  **`Sobrenome`** Sobrenome da pessoa.

*  **`Cpf`** CPf da pessoa, deve conter 11 caracteres.

*  **`Email`** Email da pessoa.


## `GET /enderecos/`

Retorna todos os endereços, não precisa de autenticação

## `POST /enderecos/`

Cria uma nova pessoa

##### PARAMS:

*  **`Logradouro`** 

*  **`Bairro`** 

*  **`Cidade`** 

*  **`Estado`** 

* **`Pessoa`** - Objeto pessoa


# IMAGENS

#### - Endpoints

![imagem1](https://i.ibb.co/VQ0RXQ1/image.png)

#### - Lista de pessoas

![imagem1](https://i.ibb.co/PT4scnj/image-1.png)


#### - Lista de enderecos

![imagem1](https://i.ibb.co/xJtpQSw/image-2.png)
