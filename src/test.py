from datetime import datetime
from autores import *
from travel import *
from activity import *
from pprint import pprint

from datetime import datetime

# Criando instâncias das classes necessárias
info = Info("João Silva", "Masculino")
feeding = Feeding(datetime(2023, 5, 1), datetime(2023, 5, 15))
hosting = Hosting(datetime(2023, 6, 1), datetime(2023, 6, 15), "Casa da Cultura")

# Criando instâncias das classes necessárias para a viagem
bsb_to_piri = government_car("Brasília", "Pirinópolis", datetime(2023, 6, 1, 8, 0, 0))
piri_to_bsb = independent_car("Pirinópolis", "Brasília", datetime(2023, 6, 15, 18, 0, 0), ["João Silva", "Maria Santos"])
origin_to_bsb = plane("Rio de Janeiro", "Brasília", datetime(2023, 5, 30, 10, 0, 0), 500.0)
bsb_to_origin = plane("Brasília", "Rio de Janeiro", datetime(2023, 6, 16, 15, 0, 0), 550.0)

# Criando um objeto Travel
travel = Travel(bsb_to_piri, piri_to_bsb, False, origin_to_bsb=origin_to_bsb, bsb_to_origin=bsb_to_origin)

# Criando uma lista de atividades
activity_list = [
    Activity("Palestra", datetime(2023, 5, 10), datetime(2023, 5, 10, 2, 0), [1, 2, 3], 1, Location("Auditório", "Rua A, 123"), Age_range(18, 65), "Educação"),
    Activity("Palestra2", datetime(2024, 5, 10), datetime(2024, 5, 10, 2, 0), [1, 2, 3], 1, Location("Casa do caralho", "Rua A, 123"), Age_range(18, 65), "Educação2")
]

# Criando um objeto Autores com os detalhes da viagem preenchidos
autor = Autores(info, feeding, activity_list, hosting, travel)
#autor = Autores((info, feeding, hosting, travel, activity_list))

objeto = autor
atributos = [attr for attr in dir(Autores) if not callable(getattr(Autores, attr)) and not attr.startswith("__")]
# regenera o dicionario
w = [getattr(objeto,a) for a in atributos]
###################################################
data = objeto.to_dict()

# atividades
activity_l = []
for a in data['activity_list']:
    activity_l.append(Activity(**a))
feeding = Feeding(**data['feeding'])
hosting = Hosting(**data['hosting'])
info = Info(**data['info'])
# travel
bsb_to_origin = 

print('ok')