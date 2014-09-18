from bs4 import BeautifulSoup
from urllib.request import urlopen
import html.parser
import re

bandex_file = urlopen('http://www.usp.br/coseas/cardapiofisica.html')
bandex_html = bandex_file.read().decode('latin1')
bandex_html = re.sub('\s{2,}', ' ', bandex_html)
bandex_file.close()

soup = BeautifulSoup(bandex_html)
table = soup.table

for string in table.stripped_strings:
    if re.search('/$', string):
        print(format(string), end='')
    else:
        print(format(string))
    

# Isso é a mais pura apelação, mas ...
# move_up = '\x1B[A'
# move_right = '\x1B[' + str(len(string)) + 'C'