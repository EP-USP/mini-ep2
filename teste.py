from urllib.request import urlopen
import html.parser
import re

class Menu(object):
	pass

class DiaDaSemana(object):
	def __init__(self, dia, almoco, janta):
		pass

def select_html_tag(tag, string):
	regex = '<' + tag + '[^>]*>(.*?)</' + tag + '[^>]*>'
	return re.findall(regex, string, re.DOTALL|re.IGNORECASE)

def get_text(html):
	lista = re.findall("(?<=>)[^ <][^<]+(?=<)", html)
	l = '\n'.join(lista)
	l = l.replace('&nbsp;', '')
	l = l.replace('/\n', '/')
	return str(l)

bandex_file = urlopen('http://www.usp.br/coseas/cardapio.html')
bandex_html = bandex_file.read().decode('latin1')
bandex_html = re.sub('\s{2,}', ' ', bandex_html)
bandex_file.close()

for tr_match in select_html_tag('tr', bandex_html):
	for td_match in select_html_tag('td', tr_match):
		print(get_text(td_match))