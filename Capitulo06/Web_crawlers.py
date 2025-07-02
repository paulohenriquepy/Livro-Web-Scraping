from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

# Criar uma função que receba um URL de um artigo da Wikipedia
# A função retorna uma lista com todos os artigos associados

# Observe que os links de páginas de artigos possuem três características:
# 1. Possuem URLs sem dois pontos
# 2. As URLs começam com /wiki/
# 3. Ao inspecionar, vemos que estão na div com o id definido como bodyContent

# Assim, mudamos o script, para remover obter apenas os artigos que desejamos
# Observe o uso de ^ para indicar artigos que não contenham tal estrutura

random.seed(int(datetime.datetime.now().timestamp()))

def getLinks(articleURL):

    html = urlopen('http://en.wikipedia.org{}'.format(articleURL))
    bs = BeautifulSoup(html, 'html.parser')

    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href = re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Charles_Darwin')

while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)