import src.wrapper_class as wrapper_class
from datetime import datetime
from src.authors import *
from src.travel import *
from src.activity import *
from src.hosting import *

# Ativando modo de depuração
wrapper_class.DEBUG = True
DataW.drop_hole_collecion()

# Funções auxiliares para criar instâncias de classes e salvar no banco
def create_author(name, gender, id_hosting):
    author = Authors(name, gender, id_hosting, datetime(1, 1, 1), datetime(9999, 1, 1))
    return author.save()

def create_location(name, address):
    location = Location(name, address)
    return location.save()

def create_activity(name, start_date, end_date, author_list, main_author, location, min_age, max_age, category):
    activity = Activity(name, start_date, end_date, author_list, main_author, location, min_age, max_age, category)
    return activity.save()

# Criando instâncias de Hosting
id_hosting = Hosting("Pousada Sítio Piri", 5, 100.0).save()

# Criando autores
id_autor1 = create_author("Beto Seabra", "Masculino", id_hosting)
id_autor2 = create_author("Maurício", "Masculino", id_hosting)
id_autor3 = create_author("Clara Arreguy", "Feminino", id_hosting)
id_autor4 = create_author("Luz Marina", "Feminino", id_hosting)
id_autor5 = create_author("Eraldo", "Masculino", id_hosting)
id_autor6 = create_author("Ângela", "Feminino", id_hosting)
id_autor7 = create_author("Iris Borges", "Feminino", id_hosting)
id_autor8 = create_author("Sérgio Pompeo", "Masculino", id_hosting)
id_autor9 = create_author("Maria das Dores Braga", "Feminino", id_hosting)
id_autor10 = create_author("Jacqueline de Mattos", "Feminino", id_hosting)
id_autor11 = create_author("Débora Bianca", "Feminino", id_hosting)
id_autor12 = create_author("Raquel", "Feminino", id_hosting)
id_autor13 = create_author("Maria Amélia", "Feminino", id_hosting)
id_autor14 = create_author("Márcia Lages", "Feminino", id_hosting)
id_autor15 = create_author("Angela B. Gê", "Feminino", id_hosting)
id_autor16 = create_author("Filipi Nascimento", "Masculino", id_hosting)
id_autor17 = create_author("André Cerino", "Masculino", id_hosting)
id_autor18 = create_author("Maria Lúcia", "Feminino", id_hosting)
id_autor19 = create_author("Eraldo e Ângela", "Masculino e Feminino", id_hosting)
id_autor20 = create_author("Márcia Lages", "Feminino", id_hosting)

# Criando locais
id_loc1 = create_location("Teatro de Pirenópolis", "Praça")
id_loc2 = create_location("Centro de Artes e Música Ita & Alaor", "Rua Principal")
id_loc3 = create_location("Pousada Sítio Piri", "Estrada Rural")
id_loc4 = create_location("Auditório Centro de Artes e Música Ita & Alaor", "Rua Principal")
id_loc5 = create_location("Colégio Comendador Joaquim Alves", "Avenida Escola")
id_loc6 = create_location("Teatro de Pirenópolis ou Espaço", "Praça")
id_loc7 = create_location("Pracinha", "Avenida Paulista")
id_loc8 = create_location("Tenda", "Praça")
id_loc9 = create_location("Teatro de Pirenópolis", "Centro")

# Criando atividades
id_ac1 = create_activity("Mesa de Debates: O que os Livros me Ensinaram", datetime(2023, 6, 13, 11, 0), datetime(2023, 6, 13, 12, 0), [id_autor1], id_autor1, id_loc1, 0, 100, "Educação")
id_ac2 = create_activity("Mesa de Debates: Livros Russos", datetime(2023, 6, 13, 11, 0), datetime(2023, 6, 13, 12, 0), [id_autor2], id_autor2, id_loc2, 0, 100, "Educação")
id_ac3 = create_activity("Mesa de Debates: Livros e Terapias de Goids", datetime(2023, 6, 13, 15, 0), datetime(2023, 6, 13, 16, 0), [id_autor3], id_autor3, id_loc3, 0, 100, "Educação")
id_ac4 = create_activity("Cerimônia de Abertura", datetime(2023, 6, 13, 18, 30), datetime(2023, 6, 13, 19, 30), [id_autor1, id_autor2, id_autor3], id_autor1, id_loc3, 0, 100, "Evento")
id_ac5 = create_activity("Show", datetime(2023, 6, 13, 19, 30), datetime(2023, 6, 13, 21, 0), [id_autor1, id_autor2], id_autor1, id_loc1, 0, 100, "Música")
id_ac7 = create_activity("Trupe dos Cirandeiros", datetime(2023, 6, 14, 8, 0), datetime(2023, 6, 14, 22, 0), [id_autor4], id_autor4, id_loc1, 0, 100, "Teatro")
id_ac8 = create_activity("Mesa de Debates: O que os Livros me Ensinaram", datetime(2023, 6, 14, 10, 0), datetime(2023, 6, 14, 11, 0), [id_autor1], id_autor1, id_loc2, 0, 100, "Educação")
id_ac10 = create_activity("Espetáculo", datetime(2023, 6, 14, 11, 0), datetime(2023, 6, 14, 12, 0), [id_autor1, id_autor2], id_autor1, id_loc2, 0, 100, "Teatro")
id_ac12 = create_activity("Contação de Histórias", datetime(2023, 6, 14, 14, 0), datetime(2023, 6, 14, 15, 0), [id_autor1], id_autor1, id_loc2, 0, 100, "Literatura")
id_ac13 = create_activity("Oficina Bebeteca", datetime(2023, 6, 14, 15, 0), datetime(2023, 6, 14, 16, 0), [id_autor1], id_autor1, id_loc2, 0, 100, "Educação")
id_ac14 = create_activity("Contação de Histórias, Brincadeiras e Canções", datetime(2023, 6, 14, 16, 0), datetime(2023, 6, 14, 17, 0), [id_autor1, id_autor2], id_autor1, id_loc2, 0, 100, "Literatura")
id_ac17 = create_activity("Show Musical", datetime(2023, 6, 14, 20, 30), datetime(2023, 6, 14, 22, 0), [id_autor1, id_autor2], id_autor1, id_loc3, 0, 100, "Música")
id_ac18 = create_activity("Oficina de Ilustração + Mesa - Encontro de Autores", datetime(2023, 6, 15, 9, 0), datetime(2023, 6, 15, 10, 30), [id_autor17], id_autor17, id_loc8, 0, 100, "Educação")
id_ac19 = create_activity("Leitura, Brincadeiras e Canções", datetime(2023, 6, 15, 9, 0), datetime(2023, 6, 15, 10, 0), [id_autor1, id_autor2, id_autor3], id_autor1, id_loc2, 0, 100, "Literatura")
id_ac21 = create_activity("Espetáculo", datetime(2023, 6, 15, 10, 0), datetime(2023, 6, 15, 11, 0), [id_autor1, id_autor2], id_autor1, id_loc1, 0, 100, "Teatro")
id_ac22 = create_activity("Un CAUSOS", datetime(2023, 6, 15, 11, 0), datetime(2023, 6, 15, 12, 0), [id_autor19], id_autor19, id_loc1, 0, 100, "Teatro")
id_ac24 = create_activity("Oficina - A Fantástica Matemática", datetime(2023, 6, 15, 9, 0), datetime(2023, 6, 15, 11, 0), [id_autor9], id_autor9, id_loc5, 0, 100, "Educação")
id_ac28 = create_activity("Contação de Histórias", datetime(2023, 6, 15, 10, 30), datetime(2023, 6, 15, 11, 0), [id_autor13], id_autor13, id_loc2, 0, 100, "Literatura")
id_ac29 = create_activity("Espetáculo - Teatro Infantil", datetime(2023, 6, 15, 11, 30), datetime(2023, 6, 15, 12, 30), [id_autor1], id_autor1, id_loc9, 0, 100, "Teatro")
id_ac30 = create_activity("Roda de Conversa", datetime(2023, 6, 15, 14, 30), datetime(2023, 6, 15, 16, 0), [id_autor20], id_autor20, id_loc7, 0, 100, "Conversa")
id_ac31 = create_activity("Espetáculo Bebeteca", datetime(2023, 6, 15, 15, 0), datetime(2023, 6, 15, 15, 30), [id_autor1], id_autor1, id_loc2, 0, 100, "Teatro")
id_ac32 = create_activity("Contação de Histórias", datetime(2023, 6, 15, 15, 30), datetime(2023, 6, 15, 16, 0), [id_autor1], id_autor1, id_loc2, 0, 100, "Literatura")
id_ac34 = create_activity("Show Bebeteca", datetime(2023, 6, 15, 16, 30), datetime(2023, 6, 15, 17, 30), [id_autor1], id_autor1, id_loc2, 0, 100, "Música")
id_ac36 = create_activity("Show de Talentos", datetime(2023, 6, 15, 18, 30), datetime(2023, 6, 15, 19, 30), [id_autor1], id_autor1, id_loc7, 0, 100, "Música")
id_ac37 = create_activity("Cerimônia de Encerramento", datetime(2023, 6, 15, 19, 30), datetime(2023, 6, 15, 20, 30), [id_autor1], id_autor1, id_loc7, 0, 100, "Evento")

# Criando viagens (exemplo)
id_trip1 = Trip("Brasília", "Pirenópolis", datetime(2024, 6, 1), "carro", 10.0, [id_autor1, id_autor2]).save()
id_trip2 = Trip("Pirenópolis", "Brasília", datetime(2024, 6, 2), "carro", 10.0, [id_autor1]).save()

print("Dados inseridos com sucesso!")
