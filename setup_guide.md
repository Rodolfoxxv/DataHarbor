# Documentação do Projeto

## Configuração Inicial

### Inicialização do Poetry

Inicializamos um novo projeto Python com o comando `poetry init`, que criou um novo arquivo `pyproject.toml` no diretório atual.

### Instalação do Python com Pyenv

Instalamos o Python 3.12.1 usando o `pyenv` com o comando `pyenv install 3.12.1` e definimos essa versão como a versão padrão do Python para o nosso ambiente atual com `pyenv local 3.12.1`.

## Configuração do Git

### Criação do .gitignore

Criamos um arquivo `.gitignore` com várias regras para ignorar certos tipos de arquivos no nosso projeto Git. Usamos o comando `touch .gitignore` para criar o arquivo e depois adicionamos as regras ao arquivo.

### Commit no Git

Adicionamos todas as alterações ao Git com `git add .` e fizemos o commit dessas alterações com `git commit -m "Initial project setup"`.

### Push no Git

Enviamos todas as nossas alterações commitadas para o repositório remoto com `git push`.

## Atualização do pyproject.toml

Atualizamos todas as dependências listadas no arquivo `pyproject.toml` para suas últimas versões compatíveis com o comando `poetry update`.

## Criação de Diretório e Arquivo

Criamos um diretório chamado `ResidentEvil` e um arquivo chamado `collect.py` dentro dele com os comandos `mkdir ResidentEvil`, `cd ResidentEvil` e `touch collect.py`.
