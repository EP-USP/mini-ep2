from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

class Menu(object):
    def __init__(self, d, m, html):
        self.day = d
        self.meal = m
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

        if self.day == 'SEGUNDA-FEIRA':
            init = list_menu.index('SEGUNDA-FEIRA')
            end = list_menu.index('TERÇA-FEIRA')
        elif self.day == 'TERÇA-FEIRA':
            init = list_menu.index('TERÇA-FEIRA')
            end = list_menu.index('QUARTA-FEIRA')
        elif self.day == 'QUARTA-FEIRA':
            init = list_menu.index('QUARTA-FEIRA')
            end = list_menu.index('QUINTA-FEIRA')
        elif self.day == 'QUINTA-FEIRA':
            init = list_menu.index('QUINTA-FEIRA')
            end = list_menu.index('SEXTA-FEIRA')
        elif self.day == 'QUINTA-FEIRA':
            init = list_menu.index('QUINTA-FEIRA')
            end = list_menu.index('SEXTA-FEIRA')
        elif self.day == 'SEXTA-FEIRA':
            init = list_menu.index('SEXTA-FEIRA')
            end = list_menu.index('SÁBADO')
        elif self.day == 'SÁBADO':
            init = list_menu.index('SÁBADO')
            end = list_menu.index('DOMINGO')
        else:
            init = list_menu.index('DOMINGO')
            end = len(list_menu) - 1

        for i in range(init, end):
            day_menu.append(list_menu[i])

        return day_menu

    def generate_meal_menu(self):
        day_menu = self.generate_day_menu()
        init_meal = [i for i, x in enumerate(day_menu) if x == self.day]
        menu = ''

        if self.meal == 'lunch':
            meal_range = range(init_meal[0] + 1, init_meal[1])
        else:
            meal_range = range(int(init_meal[1]) + 1, len(day_menu))

        for i in meal_range:
            partial = day_menu[i]
            partial += '\n'
            if not partial[0].isupper() and not partial[0].isdigit():
                menu = menu[:len(menu) - 1]
            menu +=  partial
        # menu = re.sub(' / ', '/', menu)
        return menu
