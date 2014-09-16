from urllib.request import urlopen
import html.parser
import re

def select_html_tag(tag, string):
	regex = '<' + tag + '[^>]*>(.*?)</' + tag + '[^>]*>'
	return re.finditer(regex, string, re.DOTALL|re.IGNORECASE)

def get_text(html):
	lista = re.findall("(?<=>)[^ <][^<]+(?=<)", html)
	print(lista)
	l = '\n'.join(lista)
	l = l.replace('&nbsp;', '')
	return str(l)

bandex_file = urlopen('http://www.usp.br/coseas/cardapio.html')
bandex_html = bandex_file.read().decode('latin1')
# print(bandex_html)
bandex_html = re.sub('\s{2,}', ' ', bandex_html)
bandex_file.close()


for tr_match in select_html_tag('tr', bandex_html):
	for td_match in select_html_tag('td', tr_match.group(1)):
		#get_text(td_match.group(1))
		print(get_text(td_match.group(1)))
