from urllib.request import urlopen
import re
from menu import Menu

class Restaurante(object):

    def __init__(self, nome):
        self.nome = nome
    
    def get_html(self):
            urls = {'central': 'http://www.usp.br/coseas/cardapio.html',
                    'fisica': 'http://www.usp.br/coseas/cardapiofisica.html',
                    'quimica': 'http://www.usp.br/coseas/cardapioquimica.html',
                    'pco': 'http://www.usp.br/coseas/cardcocesp.html'}
            try:
                url = urls[self.nome]
                bandex_file = urlopen(url)
                bandex_html = bandex_file.read().decode('latin1')
                bandex_html = re.sub('\s{2,}', ' ', bandex_html)
                bandex_file.close()
                return bandex_html
            except KeyError:
                print('Nome de bandeijao invalido')
            finally:
                exit()

    def get_menu(self, d, m):
        menu = Menu(d, m, self.get_html())
        print(menu.generate_meal_menu())
