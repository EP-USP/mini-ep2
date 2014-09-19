from bs4 import BeautifulSoup
from urllib.request import urlopen
import html.parser
import re
import argparse
import datetime
from restaurante import Restaurante

def day_of_week(day_number):

    day_list = ['segunda', 'terca', 'quarta',
                'quinta', 'sexta', 'sabado',
                'domingo']
    return day_list[day_number]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    day_number = datetime.datetime.today().weekday()

    parser = argparse.ArgumentParser(fromfile_prefix_chars='@')

    parser.add_argument('-b', '--bandex', help='Local')
    parser.add_argument('-d', '--dia', help='Dia da semana', default=day_of_week(day_number))
    parser.add_argument('-a', '--almoco', help='Almoço', action='store_true')
    parser.add_argument('-j', '--janta', help='Janta', action='store_true')

    args = parser.parse_args()
    if not args.bandex:
    	args = parser.parse_args(['@.bandexrc'])

    restaurante = Restaurante(args.bandex)
    if not args.almoco and not args.janta:
        restaurante.print_menu(args.dia, True, True)
    else:
        restaurante.print_menu(args.dia, args.almoco, args.janta)

