from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import re

# Aprendendo a estrutura de navegação em árvores

# Encontrando apenas os descendentes que são filhos
# Utilizamos o método .children

'''html = urlopen('https://floradobrasil.jbrj.gov.br/reflora/listaBrasil/ConsultaPublicaUC/BemVindoConsultaPublicaConsultar.do?invalidatePageControlCounter=1&idsFilhosAlgas=%5B2%5D&idsFilhosFungos=%5B1%2C11%2C10%5D&lingua=&grupo=6&familia=null&genero=Adiantum&especie=&autor=&nomeVernaculo=&nomeCompleto=&formaVida=null&substrato=null&ocorreBrasil=QUALQUER&ocorrencia=OCORRE&endemismo=TODOS&origem=TODOS&regiao=QUALQUER&estado=QUALQUER&ilhaOceanica=32767&domFitogeograficos=QUALQUER&bacia=QUALQUER&vegetacao=TODOS&mostrarAte=SUBESP_VAR&opcoesBusca=TODOS_OS_NOMES&loginUsuario=Visitante&senhaUsuario=&contexto=consulta-publica')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('tbody').children:
    print(child)'''

# Lidando com irmãos

# A função next_siblings() facilita a coleta de dados de tabelas,
# em especial, aquelas com linhas de títulos

'''html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)'''

# Lidando com pais

'''html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs.find('img',
              {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())'''

# Usando expressões regulares

'''html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

imagens = bs.find_all('img',
                      {'src': re.compile('../img/gifts/img.*.jpg')})

for imagem in imagens:
    print(imagem['src'])'''

