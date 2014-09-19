from bs4 import BeautifulSoup
from urllib.request import urlopen

class Menu(object):

    def __init__(self, d, m):
        self.day = d
        self.meal = m

    def generate_list_menu(self, raw_menu):

        soup = BeautifulSoup(bandex_html)
        table = soup.table

        list_menu = []

        for string in table.stripped_strings:
            list_menu.append(string)

        return list_menu

    def generate_day_menu(self, list_menu):
        
        day_menu = []

        if day == 'SEGUNDA-FEIRA':
            init = list_menu.index('SEGUNDA-FEIRA')
            end = list_menu.index('TERÇA-FEIRA')
        elif day == 'TERÇA-FEIRA':
            init = list_menu.index('TERÇA-FEIRA')
            end = list_menu.index('QUARTA-FEIRA')
        elif day == 'QUARTA-FEIRA':
            init = list_menu.index('QUARTA-FEIRA')
            end = list_menu.index('QUINTA-FEIRA')
        elif day == 'QUINTA-FEIRA':
            init = list_menu.index('QUINTA-FEIRA')
            end = list_menu.index('SEXTA-FEIRA')
        elif day == 'QUINTA-FEIRA':
            init = list_menu.index('QUINTA-FEIRA')
            end = list_menu.index('SEXTA-FEIRA')
        elif day == 'SEXTA-FEIRA':
            init = list_menu.index('SEXTA-FEIRA')
            end = list_menu.index('SÁBADO')
        elif day == 'SÁBADO':
            init = list_menu.index('SÁBADO')
            end = list_menu.index('DOMINGO')
        else:
            init = list_menu.index('DOMINGO')
            end = list_menu[len(list_menu) - 1]

        for i in range(init, end):
            day_menu.append(list_menu[i])

        return day_menu

    def generate_meal_menu(self, day_menu):
        
        init_meal = [i for i, x in enumerate(day_menu) if x == day]
        
        if meal == 'lunch':
            for i in range(init_meal):
                print(day_menu[i])
        else:
            for i in range(init_meal[1], day_menu[len(day_menu) - 1]):
                print(day_menu[i])


