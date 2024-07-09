import wrapper_class
from authors import *
from travel import *
from activity import *
from hosting import *
from category import *
from datetime import datetime
from aditional_cost import AditionalCost


wrapper_class.DEBUG = True
DataW.drop_hole_collecion()

# Categorias
id_itinerancia = Category("Itinerância", 500.0).save()

# Criação de locais
id_praca = Location("Praça / Zazá Café", "Praça Central").save()
id_teatro_ = Location("Teatro de Pirenópolis", "Centro da Cidade").save()

id_hosting = Hosting("Pousada padrão", 100, 50.0).save()

# Criação de autores (simplificado, sem hospedagem)
autores = {}
for nome in [
                "Mauricio", 
                "Clara Arreguy", 
             ]:
    autores[nome] = Authors(nome, "Não especificado", id_hosting, datetime(year=2023,month=6,day=12), datetime(year=2023,month=6,day=16)).save()

# Criação de atividades
# 12 de Junho
Activity("Sarau Literário / Lançamento de livros", datetime(2023, 6, 12, 20, 0), datetime(2023, 6, 12, 22, 0), [autores["Mauricio"]], autores["Mauricio"], id_praca, 0, 100, id_itinerancia).save()

id_trip1 = Trip("brasilia", "piri", datetime(2025, 6, 1), "Carro", 10.0, [autores["Mauricio"]]).save()

AditionalCost("ABERTURA", 1000.0).save()

DataW.set_meal_price(10.5)

print("ok")