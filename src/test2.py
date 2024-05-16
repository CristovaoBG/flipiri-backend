import wrapper_class
from datetime import datetime
from autores import *
from travel import *
from activity import *
from pprint import pprint
from dataclasses import asdict
from datetime import datetime
from bson import ObjectId
from hosting import *

wrapper_class.DEBUG = True  # feio, mas um pouco mais seguro

# cria primeiro autor
id_feeding = Feeding(datetime(2023, 5, 1), datetime(2023, 5, 15)).save()
autor = Autores("João Silva", "Masculino", id_feeding)
id_autor1 = autor.save()

# outro autor
id_feeding = Feeding(datetime(2023, 5, 1), datetime(2023, 5, 15)).save()
autor = Autores("Ana Souza", "Feminino", id_feeding)
id_autor2 = autor.save()

# primeira atividade
id_loc = Location("Auditório", "Rua A, 123").save()
id_agerange = AgeRange(0,10).save()
autor_list = [id_autor1]
id_ac1 = Activity("Palestra", datetime(2023, 5, 10), datetime(2023, 5, 10, 2, 0), autor_list, id_autor1, id_loc, id_agerange, "Educação").save()

# segunda atividade
id_loc = Location("Pracinha", "Avenida Paulista")
autor_list = [id_autor1, id_autor2]
id_agerange = AgeRange(18,100)
id_ac2 = Activity("Palestra", datetime(2023, 5, 10), datetime(2023, 5, 10, 2, 0), autor_list, id_autor2, id_loc, id_agerange, "Bronhasso").save()

# viagens
id_trip1 = Trip("brasilia", "piri", datetime(2025, 6, 1), "carro", 10.0, [id_autor1, id_autor2]).save()
id_trip2 = Trip("piri", "brasilia", datetime(2026, 7, 2), "carro", 15.0, [id_autor1]).save()
id_trip3 = Trip("rio", "sp", datetime(2025, 8, 10), "avião", 20.0, [id_autor2]).save()
id_trip4 = Trip("sp", "rio", datetime(2026, 9, 20), "ônibus", 25.0, []).save()

# hospedagem
id_hosting = Hosting(datetime(2025, 6, 1),datetime(2025, 6, 3), "Naquele Lugar", 5, 50.0, [id_autor1, id_autor2]).save()

# imprime as coisa tudo
print("ok")
