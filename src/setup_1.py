import wrapper_class
from authors import *
from travel import *
from activity import *
from hosting import *
from datetime import datetime


wrapper_class.DEBUG = True  # feio, mas um pouco mais seguro

# hospedagem
id_hosting = Hosting(
                     "Naquele Lugar",
                     5,
                     100.0
                     ).save()

# cria primeiro autor
autor = Authors("João Silva", "Masculino",id_hosting, datetime(1,1,1), datetime(9999,1,1))
id_autor1 = autor.save()

# outro autor
autor = Authors("Ana Souza", "Feminino", id_hosting, datetime(1,1,1), datetime(9999,1,1))
id_autor2 = autor.save()

# primeira atividade
id_loc = Location("Auditório", "Rua A, 123").save()
id_ac1 = Activity("Palestra",                   # activity name
                  datetime(2023, 5, 10),        # time start
                  datetime(2023, 5, 10, 2, 0),  # time end
                  [id_autor1],                  # authors involved
                  id_autor1,                    # responsible author
                  id_loc,                       # location
                  0,                            # minimum age
                  10,                           # maximum age
                  "Educação"                    # category
                  ).save()

# segunda atividade
id_loc = Location("Pracinha", "Avenida Paulista").save()
autor_list = id_ac2 = Activity("Palestra",
                  datetime(2023, 5, 11),
                  datetime(2023, 5, 11, 2, 0),
                  [id_autor1, id_autor2],
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

# imprime as coisa tudo
print("ok")
