from bs4 import BeautifulSoup
from urllib.request import urlopen
import html.parser
import re
import argparse
import datetime
from restaurante import Restaurante

def day_of_week(day_number):
	
	if day_number == 0:
		return 'segunda'
	elif day_number == 1:
		return 'terca'
	elif day_number == 2:
		return 'quarta'
	elif day_number == 3:
		return 'quinta'
	elif day_number == 4:
		return 'sexta'
	elif day_number == 5:
		return 'sabado'
	else:
		return 'domingo'


day_number = datetime.datetime.today().weekday()
parser = argparse.ArgumentParser(fromfile_prefix_chars='@')

parser.add_argument('-b', '--bandex', help='Local')
parser.add_argument('-d', '--dia', help='Dia da semana', default=day_of_week(day_number))
parser.add_argument('-a', '--almoco', help='Almoço', action='store_true')
parser.add_argument('-j', '--janta', help='Janta', action='store_true')

args = parser.parse_args()
if (not args.bandex):
	args = parser.parse_args(['@.bandexrc'])

restaurante = Restaurante(args.bandex)
restaurante.get_menu('SEGUNDA-FEIRA', 'lunch')

