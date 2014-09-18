from bs4 import BeautifulSoup
from urllib.request import urlopen
import html.parser
import re
import argparse

def main():

	parser = argparse.ArgumentParser()

	parser.add_argument("-b", "--bandex", help="Local")
	parser.add_argument("-d", "--dia", help="Dia da semana")
	parser.add_argument("-a", "--almoco", help="Almoço")
	parser.add_argument("-j", "--janta", help="Janta")

	args = parser.parse_args()

	raw_menu = generate_raw_menu(args.bandex)

# Gera um cardapio 'bruto' em html para o bandejao escolhido pelo usuario
def generate_raw_menu(self, bandex):

	if bandex == 'central':
		url = 'http://www.usp.br/coseas/cardapio.html'
	elif bandex == 'fisica':
		url = 'http://www.usp.br/coseas/cardapiofisica.html'
	elif bandex == 'quimica':
		url = 'http://www.usp.br/coseas/cardapioquimica.html'
	else
		url = 'http://www.usp.br/coseas/cardcocesp.html'

	bandex_file = urlopen(url)
	bandex_html = bandex_file.read().decode('latin1')
	bandex_html = re.sub('\s{2,}', ' ', bandex_html)
	bandex_file.close()

	return bandex_html

# Gera uma lista, contendo os itens do cardapio da semana, a partir de um cardapio 'bruto'
def generate_list_menu(self, raw_menu):

	soup = BeautifulSoup(bandex_html)
	table = soup.table

	list_menu = []

	for string in table.stripped_strings:
    	list_menu.append(string)

    return list_menu

