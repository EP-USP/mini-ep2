from restaurante import Restaurante
from testes.teste import Teste, FalhouNoTeste
from testes.tester import Tester

class BandecoTest(Teste):

	def compare(self, string1, string2):
		if string1 == string2:
			print('O teste passou com sucesso!')
		else:
			print('O teste falhou! =(')
			raise FalhouNoTeste

	def run(self):

		mon_lunch_central = 'Arroz/feijão/arroz integral\n' + \
							'Hambúrguer barbecue\n' + \
							'Creme de milho\n' + \
							'Salada de escarola\n' + \
							'Opcional: PVT com legumes\n' + \
							'Bananinha/refresco\n' + \
							'Valor calórico de 1 refeição 1055 kcal'

		sat_lunch_phys = 'FECHADO'

		wed_dinner_chem = 'Arroz/Feijão/Arroz integral\n' + \
							'Peixe ao forno\n' + \
							'Chuchu na salsa\n' + \
							'Salada de alface\n' + \
							'Opcional: Quibe de PVT\n' + \
							'Mamão\n' + \
							'Refresco\n' + \
							'876 kcal'

		fri_lunch_pco = 'Arroz/feijão/arroz integral\n' + \
							'Tiras de carne à cigana\n' + \
							'Mandioca corada\n' + \
							'Salada de almeirão\n' + \
							'Opcional: Bolinho de PVT ao molho shoyo\n' + \
							'Maçã/refresco\n' + \
							'Valor calórico de 1 refeição 829 kcal'

		fri_dinner_pco = 'Fechado'

		rest_central = Restaurante('central')
		rest_fisica = Restaurante('fisica')
		rest_quimica = Restaurante('quimica')
		rest_pco = Restaurante('pco')

		print('Comparando - Bandejão central - Segunda-feira - Almoço:')
		self.compare(rest_central.print_menu('segunda', True, False), mon_lunch_central)
		print(mon_lunch_central)
		print('Comparando - Bandejão da Física - Sábado - Almoço:')
		self.compare(rest_fisica.print_menu('sabado', True, False), sat_lunch_phys)
		print(sat_lunch_phys)
		print('Comparando - Bandejão da Química - Quarta-feira - Janta:')
		self.compare(rest_quimica.print_menu('quarta', False, True), wed_dinner_chem)
		print(wed_dinner_chem)
		print('Comparando - Bandejão PCO - Sexta-feira - Almoço:')
		self.compare(rest_pco.print_menu('sexta', True, False), fri_lunch_pco)

		print('Comparando - Bandejão PCO - Sexta-feira - Janta:')
		self.compare(rest_pco.print_menu('sexta', False, True), fri_dinner_pco)

		print('Testando para um restaurante desconhecido:')

		try:
			fake = Restaurante('fake', False, False)
			print('O teste falhou! =(')
		except:
			print('O teste passou com sucesso!')

class BandecoTester(Tester):

	def __init__(self):
		teste = BandecoTest()
		self.testes = [teste]

if __name__ == '__main__':
	tester = BandecoTester()
	tester.test()
