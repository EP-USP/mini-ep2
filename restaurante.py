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
                bandex_html = bandex_html.replace('OBSERVAÇÃO:', 'OBSERVAÇÃO')
                bandex_file.close()
                return bandex_html
            except KeyError:
                print('Nome de bandeijao invalido')
                raise

    def print_menu(self, d, print_lunch, print_dinner):
        retorno = ''
        if print_lunch:
            print('---Almoço---')
            menu = Menu(d, True, self.get_html())
            menu_meal = menu.generate_meal_menu()
            retorno += menu_meal
            print(menu_meal)
        if print_dinner:
            if print_lunch:
                retorno += ' '
            print('---Janta---')
            menu = Menu(d, False, self.get_html())
            menu_meal = menu.generate_meal_menu()
            retorno += menu_meal
            print(menu_meal)
        return retorno

