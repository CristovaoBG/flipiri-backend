import wrapper_class
from datetime import datetime
from authors import *
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
autor = Authors("João Silva", "Masculino", id_feeding)
id_autor1 = autor.save()

# outro autor
id_feeding = Feeding(datetime(2023, 5, 1), datetime(2023, 5, 15)).save()
autor = Authors("Ana Souza", "Feminino", id_feeding)
id_autor2 = autor.save()

# primeira atividade
id_loc = Location("Auditório", "Rua A, 123").save()
autor_list = [id_autor1]
id_ac1 = Activity("Palestra",
                  datetime(2023, 5, 10),
                  datetime(2023, 5, 10, 2, 0),
                  autor_list,
                  id_autor1,
                  id_loc,
                  0,
                  10,
                  "Educação"
                  ).save()

# segunda atividade
id_loc = Location("Pracinha", "Avenida Paulista").save()
autor_list = [id_autor1, id_autor2]
id_ac2 = Activity("Palestra",
                  datetime(2023, 5, 10),
                  datetime(2023, 5, 10, 2, 0),
                  autor_list,
                  id_autor2,
                  id_loc,
                  18,
                  100,
                  "Bronhasso"
                  ).save()

# viagens
id_trip1 = Trip("brasilia", "piri", datetime(2025, 6, 1), "carro", 10.0, [id_autor1, id_autor2]).save()
id_trip2 = Trip("piri", "brasilia", datetime(2026, 7, 2), "carro", 15.0, [id_autor1]).save()
id_trip3 = Trip("rio", "sp", datetime(2025, 8, 10), "avião", 20.0, [id_autor2]).save()
id_trip4 = Trip("sp", "rio", datetime(2026, 9, 20), "ônibus", 25.0, []).save()

# hospedagem
id_hosting = Hosting(datetime(2025, 6, 1),
                     datetime(2025, 6, 3),
                     "Naquele Lugar",
                     [id_autor1, id_autor2],
                     5,
                     500.0
                     ).save()

# imprime as coisa tudo
print("ok")
