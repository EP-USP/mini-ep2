from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

class Menu(object):
    def __init__(self, d, isLunch, html):
        self.day = d
        self.isLunch = isLunch
        self.html = html

    def generate_list_menu(self):

        soup = BeautifulSoup(self.html)
        table = soup.table

        list_menu = []

        for string in table.stripped_strings:
            list_menu.append(string)

        return list_menu

    def generate_day_menu(self):
        list_menu = self.generate_list_menu();
        day_menu = []
        closing_tag = 'OBSERVAÇÃO'
        keys = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
        day_tags = {'segunda': 'SEGUNDA-FEIRA',
                    'terca': 'TERÇA-FEIRA',
                    'quarta': 'QUARTA-FEIRA',
                    'quinta': 'QUINTA-FEIRA',
                    'sexta': 'SEXTA-FEIRA',
                    'sabado': 'SÁBADO',
                    'domingo': 'DOMINGO',
                    'end': 'O'}
        try:
            init_tag = day_tags[self.day]
            self.day_tag = init_tag
        except KeyError:
            print('dia da semana inexistente')
            raise
        print(list_menu)
        init = list_menu.index(init_tag)
        try:
            end_index = keys.index(self.day) + 1
            end_tag = day_tags[keys[end_index]]
            end = list_menu.index(end_tag)
        except:
            end = list_menu.index(closing_tag)
        return list_menu[init:end]

    def generate_meal_menu(self):
        day_menu = self.generate_day_menu()
        init_meal = [i for i, x in enumerate(day_menu) if x == self.day_tag]
        menu = ''
        if self.isLunch:
            init_range = init_meal[0] + 1
            if len(init_meal) > 1:
                end_range = init_meal[1]
            else:
                end_range = len(day_menu)
            meal_range = range(init_range, end_range)
        else:
            try:
                meal_range = range(int(init_meal[1]) + 1, len(day_menu))
            except:
                return 'FECHADO'
        for i in meal_range:
            partial = day_menu[i]
            partial += '\n'
            if not partial[0].isupper() and not partial[0].isdigit():
                menu = menu[:len(menu) - 1]
            menu +=  partial
        # menu = re.sub(' / ', '/', menu)
        return menu
