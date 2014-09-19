from urllib.request import urlopen
import re
from menu import Menu

class Restaurante(object):
    def __init__(self, name):
        self.name = name

	def get_html(self):
			if self.name == 'central':
	    		url = 'http://www.usp.br/coseas/cardapio.html'
			elif self.name == 'fisica':
	    		url = 'http://www.usp.br/coseas/cardapiofisica.html'
			elif self.name == 'quimica':
	    		url = 'http://www.usp.br/coseas/cardapioquimica.html'
			else:
	    		url = 'http://www.usp.br/coseas/cardcocesp.html'

			bandex_file = urlopen(url)
			bandex_html = bandex_file.read().decode('latin1')
			bandex_html = re.sub('\s{2,}', ' ', bandex_html)
			bandex_file.close()

			return bandex_html

    def get_menu(self, d, m):
        menu = Menu(d, m, self.get_html())
        print(menu.generate_meal_menu())
