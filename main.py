from bs4 import BeautifulSoup
from urllib.request import urlopen
import html.parser
import re
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-b', '--bandex', help='Local')
parser.add_argument('-d', '--dia', help='Dia da semana')
parser.add_argument('-a', '--almoco', help='Almoço')
parser.add_argument('-j', '--janta', help='Janta')

args = parser.parse_args()

# Gera um cardapio 'bruto' em html para o bandejao escolhido pelo usuario

if args.bandex == 'central':
    url = 'http://www.usp.br/coseas/cardapio.html'
elif args.bandex == 'fisica':
    url = 'http://www.usp.br/coseas/cardapiofisica.html'
elif args.bandex == 'quimica':
    url = 'http://www.usp.br/coseas/cardapioquimica.html'
else:
    url = 'http://www.usp.br/coseas/cardcocesp.html'

bandex_file = urlopen(url)
bandex_html = bandex_file.read().decode('latin1')
bandex_html = re.sub('\s{2,}', ' ', bandex_html)
bandex_file.close()

# Gera uma lista, contendo os itens do cardapio da semana, a partir de um cardapio 'bruto'
soup = BeautifulSoup(bandex_html)
table = soup.table

list_menu = []

for string in table.stripped_strings:
    list_menu.append(string)

# Tratar aqui o list_menu
# ex. se tiver um / em list_menu[i], juntar as strings list_menu[i-1] e list_menu[i+1]
# etc...

# Gera uma lista contendo apenas o dia solicitado pelo usuario
if args.dia == 'segunda':
    init = list_menu.index('SEGUNDA-FEIRA')
    end = list_menu.index('TERÇA-FEIRA')
    for i in range(init, end):
        print(list_menu[i])
# Repetir a estrategia para os outros dias...