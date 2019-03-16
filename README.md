# Desafio realizado para seleção na Stefanini

# Instaçaão
## Passo 1: Dentro da pasta challenge-stefanini, rodar `utils.sh` com o seguinte comando `source ./utils.sh`, script inicializa a virtual-env. 


# API Documentation for challenge.

## `GET /pessoas/`

Retorna todas as pessoas, no precisa de autenticação

## `GET /enderecos/`

Retorna todos os endereços, não precisa de autenticação

## `POST /pessoas/`

Cria uma nova pessoa

##### PARAMS:

*  **`Nome`** nome da pessoa

*  **`Sobrenome`** Sobrenome da pessoa.

*  **`Cpf`** CPf da pessoa, deve conter 11 caracteres.

*  **`Email`** Email da pessoa.
