import ssl
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# O objetivo é criar um script simples para obter o título de uma página de notícias

# Criar contexto SSL que ignora verificação de certificado
ssl_context = ssl._create_unverified_context()

def getTitle(url):

    # Tenta abrir uma página e obter o arquivo HTML
    # Se der erro, retorna None

    try:
        html = urlopen(url, context=ssl_context)
    except HTTPError as e:
        return None
    except Exception as e:
        print("Erro ao acessar:", e)
        return None

    # Tenta obter uma tag da página
    # Se der erro, retorna None

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError:
        return None

    return title

title = getTitle('https://www.gov.br/mma/pt-br/search?origem=form&SearchableText=clima')

if title is None:
    print("O título não pôde ser encontrado")
else:
    print(title)
