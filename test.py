class Test(object):
	
	def compare(self, string1, string2):
		if string1 == string2:
			print('O teste passou com sucesso!')
		else
			print('O teste falhou! =(')

	def main():
		
		mon_lunch_central = 'Arroz/feijão/arroz integral\n\
		Hambúrguer barbecue\n\
		Creme de milho\n\
		Salada de escarola\n\
		Opcional: PVT com legumes\n\
		Bananinha/refresco\n\
		Valor calórico de 1 refeição 1055 kcal'

		sat_lunch_phys = 'FECHADO'

		wed_dinner_chem = 'Arroz/Feijão/Arroz integral\n\
		Peixe ao forno\n\
		Chuchu na salsa\n\
		Salada de alface\n\
		Opcional: Quibe de PVT\n\
		Mamão\n\
		Refresco\n\
		876 kcal'

		fri_lunch_pco = 'Arroz/feijão/arroz integral\n\
		Tiras de carne à cigana\n\
		Mandioca corada\n\
		Salada de almeirão\n\
		Opcional: Bolinho de PVT ao molho shoyo\n\
		Maçã/refresco\n\
		Valor calórico de 1 refeição 829 kcal'

		fri_dinner_pco = 'Fechado'

		rest_central = Restaurante('central')
		rest_fisica = Restaurante('fisica')
		rest_quimica = Restaurante('quimica')
		rest_pco = Restaurante('pco')

		compare(rest_central.get_menu('segunda', 'almoco'), mon_lunch_central)
		compare(rest_fisica.get_menu('sabado', 'almoco'), sat_lunch_phys)
		compare(rest_quimica.get_menu('quarta', 'janta'), wed_dinner_chem)
		compare(rest_pco.get_menu('sexta', 'almoco'), fri_lunch_pco)
		compare(rest_pco.get_menu('sexta', 'janta'), fri_dinner_pco)

