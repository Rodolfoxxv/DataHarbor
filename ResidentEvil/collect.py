import requests
from bs4 import BeautifulSoup

#Criando varivel que define a pagina que vai ser acessada
url = 'https://www.residentevildatabase.com/personagens/ada-wong/' 

#Definindo headers e informando a pagina o qual navegardor está acessando ela
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'pt-BR,pt;q=0.6',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Brave";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

#Recebendo a reposta html e mostrando a resposta 
resp = requests.get(url, headers=headers)
resp.status_code
print(resp.status_code)

#Usando a biblioteca BeautifulSoup para estruturar a pagina
soup = BeautifulSoup(resp.text)
print(soup)