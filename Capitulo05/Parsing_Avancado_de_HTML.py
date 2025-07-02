from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

# Obtendo todos os elementos de uma tag específica


'''html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

# Obtendo uma lista com os conteúdos de um determinado tipo de tag
nameList = bs.find_all('span', {'class':'green'})
for name in nameList:
    print(name.get_text())'''

# Obtendo todas as tags de títulos de uma página da Wikipedia

'''html = urlopen('https://en.wikipedia.org/wiki/Pharmacology')
bs = BeautifulSoup(html.read(), 'html.parser')
titulos = bs.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
for titulo in titulos:
    print(titulo.get_text())'''






