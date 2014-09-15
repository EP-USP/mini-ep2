import urllib2
import re

bandex_file = urllib2.urlopen('http://www.usp.br/coseas/cardapio.html')
bandex_html = bandex_file.read()
bandex_file.close()

ugly_list = re.findall("(?<=>)[^<]+(?=<)", bandex_html)
beautiful_list = []

for item in ugly_list:
	if (item != '\n'):
		f = item.replace('\n', ' ')
		f = re.sub('\s+', ' ', f)
		if f != ' ':
			beautiful_list.append(f)
			
for item in beautiful_list:
	print format(item)