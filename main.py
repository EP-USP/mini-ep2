from bs4 import BeautifulSoup
from urllib.request import urlopen
import html.parser
import re
import argparse
from restaurante import Restaurante

parser = argparse.ArgumentParser()

parser.add_argument('-b', '--bandex', help='Local')
parser.add_argument('-d', '--dia', help='Dia da semana')
parser.add_argument('-a', '--almoco', help='Almoço', action='store_true')
parser.add_argument('-j', '--janta', help='Janta', action='store_true')

args = parser.parse_args()

restaurante = Restaurante(args.bandex)
restaurante.get_menu('DOMINGO', 'lunch')

