# Documentação do Projeto ResidentEvil

## Configuração Inicial

### Instalação da biblioteca requests

Instalamos a biblioteca `requests` no nosso projeto Python usando o Poetry com o comando `poetry add requests`. A biblioteca `requests` permite que façamos requisições HTTP em nosso código Python.

### Criação do arquivo collect.py

Criamos um arquivo chamado `collect.py` dentro da pasta `ResidentEvil`. Este arquivo será usado para coletar dados.

## Código Atual

No arquivo `collect.py`, temos o seguinte código:

```python
import requests

url = 'https://www.google.com'
try:
    resp = requests.get(url, timeout=10)
    print(resp.status_code)
except requests.exceptions.Timeout:
    print("A solicitação excedeu o tempo limite")
