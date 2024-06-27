from datetime import datetime, timedelta
import src.wrapper_class as wrapper_class
from src.authors import *
from src.activity import *
from pprint import pprint
from dataclasses import asdict
from bson import ObjectId

wrapper_class.DEBUG = True
DataW.drop_hole_collecion()

def create_author(name):
    return Authors(name, "", None, datetime(1,1,1), datetime(9999,12,31)).save()

def create_activity(name, date, time, duration, authors, location, category):
    start_time = datetime.combine(date, time)
    end_time = start_time + timedelta(hours=duration)
    return Activity(name, 
                    start_time, 
                    end_time,
                    authors, 
                    authors[0], 
                    location, 
                    0, 
                    100,  # Capacidade estimada
                    category)

# Criação de locais
locations = {
    "praca_zaza": Location("Praça / Zazá Café", "").save(),
    "teatro_pirenopolis": Location("Teatro de Pirenópolis", "").save(),
    "teatro_pirenopolis_2": Location("Teatro de Pirenópolis - Sala 2", "").save(),
    "palco_centro_artes": Location("Palco - Centro de Artes e Música Itá", "").save(),
    "palco_centro_artes_2": Location("Palco - Centro de Artes e Música Itá - Área 2", "").save(),
    "tenda": Location("Tenda", "").save(),
    "pousada_sta_barbara": Location("Pousada Stª Bárbara", "").save(),
    "pousada_sta_barbara_2": Location("Pousada Stª Bárbara - Sala 2", "").save(),
    "espaco": Location("Teatro de Pirenópolis ou Espaço", "").save(),
    "palco_igreja": Location("Palco da igreja", "").save(),
    "musica_ita_alior": Location("Música Itá e Alior", "").save(),
    "musica_ita_alior_2": Location("Música Itá e Alior - Área 2", "").save(),
    "auditorio_centro_artes": Location("Auditório do Centro de Artes", "").save(),
    "saindo_tenda": Location("Saindo da Tenda", "").save(),
    "palco_bebeteca": Location("Palco - Centro de Artes e Música Itá e Alior", "").save(),
    "praca": Location("Praça", "").save(),
    "caminhada_turistica": Location("Caminhada aos pontos turísticos, partindo da Tenda", "").save(),
    "colegio_joaquim_alves": Location("Colégio Comendador Joaquim Alves", "").save(),
    "colegio_joaquim_alves_2": Location("Colégio Comendador Joaquim Alves - Sala 2", "").save(),
    "colegio_joaquim_alves_3": Location("Colégio Comendador Joaquim Alves - Sala 3", "").save(),
    "colegio_joaquim_alves_4": Location("Colégio Comendador Joaquim Alves - Sala 4", "").save(),
    "bebeteca_sala": Location("Bebeteca sala - Centro de Artes e Música Itá e Alior", "").save(),
}

# Criação de autores (como antes)
authors = {name: create_author(name) for name in [
    "Sarau Literário", "Beto Seabra", "Mauricio", "Clara Arreguy", "Aplam", "Todos",
    "Luz Marina", "Rose Costa", "Celia", "Reconito", "Priscila Sabino e Amanda Luz", "Iris Borges",
    "Mediadora Anna Amélia Eloi", "Ana Neila", "ICAE Umbanda", "Liduina, Iris, Maurício e Clara",
    "Turma do Caracol", "Débora Bianca", "Matrakaberta (Adriana Maciel)", "CHIQUITAS & BACANAS",
    "Angela", "André Cerino", "Ilustradores", "Tricontando (Ana Neila, Rose Costa e Hozana)",
    "Hozana Costa", "Reconito (Liduina com o Grupo Reconito)", "Uris CAUSOS", "Eraldo e Angela",
    "Iris Borges e Sérgio Pompeo", "Maria das Dores Brigagão", "Jacqueline de Mattos", "Débora Bianca",
    "Raquel", "Maria Amélia", "SANEAGO", "Marcia Lages", "Turma do Caracol (Maria e André Cerino)",
    "Cinco escritores-membros da Flipiri", "Angela B. Café", "Diretoria da Casa de Autores e colaboradores",
    "Marcelo Barra"
]}

# Criação de atividades

# 12 de Junho
create_activity("Sarau Literário / Lançamento de livros", datetime(2023, 6, 12).date(), datetime.strptime("20:00", "%H:%M").time(), 2, [authors["Sarau Literário"]], locations["praca_zaza"], "Literatura").save()

# 13 de Junho
create_activity("Mesa de Debates: O que os Livros me Ensinaram", datetime(2023, 6, 13).date(), datetime.strptime("11:00", "%H:%M").time(), 2, [authors["Beto Seabra"]], locations["teatro_pirenopolis"], "Debate").save()
create_activity("Mesa Russos", datetime(2023, 6, 13).date(), datetime.strptime("11:00", "%H:%M").time(), 2, [authors["Mauricio"]], locations["palco_centro_artes"], "Debate").save()
create_activity("Mesa de Debates: O que os Livros trazem de Goiás", datetime(2023, 6, 13).date(), datetime.strptime("16:00", "%H:%M").time(), 2, [authors["Clara Arreguy"]], locations["palco_centro_artes"], "Debate").save()
create_activity("Lançamento de livro", datetime(2023, 6, 13).date(), datetime.strptime("17:00", "%H:%M").time(), 1, [authors["Todos"]], locations["tenda"], "Literatura").save()
create_activity("Cerimônia de Abertura", datetime(2023, 6, 13).date(), datetime.strptime("19:00", "%H:%M").time(), 1, [authors["Todos"]], locations["pousada_sta_barbara"], "Cerimônia").save()

# 14 de Junho
create_activity("Trupe dos Cirandeiros", datetime(2023, 6, 14).date(), datetime.strptime("08:00", "%H:%M").time(), 14, [authors["Luz Marina"]], locations["espaco"], "Performance").save()
create_activity("Pipa literária", datetime(2023, 6, 14).date(), datetime.strptime("10:00", "%H:%M").time(), 1, [authors["Rose Costa"]], locations["palco_igreja"], "Literatura").save()
create_activity("Espetáculo", datetime(2023, 6, 14).date(), datetime.strptime("09:30", "%H:%M").time(), 0.5, [authors["Celia"]], locations["musica_ita_alior"], "Espetáculo").save()
create_activity("Espetáculo", datetime(2023, 6, 14).date(), datetime.strptime("10:00", "%H:%M").time(), 1, [authors["Reconito"]], locations["musica_ita_alior_2"], "Espetáculo").save()
create_activity("Musicalização", datetime(2023, 6, 14).date(), datetime.strptime("10:00", "%H:%M").time(), 0.5, [authors["Priscila Sabino e Amanda Luz"]], locations["palco_bebeteca"], "Música").save()
create_activity("Contação de histórias para bebês", datetime(2023, 6, 14).date(), datetime.strptime("10:30", "%H:%M").time(), 0.5, [authors["Iris Borges"]], locations["bebeteca_sala"], "Contação de Histórias").save()
create_activity("Mesa de Debates: Literatura e Ascensão Social", datetime(2023, 6, 14).date(), datetime.strptime("11:00", "%H:%M").time(), 1, [authors["Mediadora Anna Amélia Eloi"]], locations["auditorio_centro_artes"], "Debate").save()
create_activity("Contação de histórias - Bebeteca", datetime(2023, 6, 14).date(), datetime.strptime("11:00", "%H:%M").time(), 0.5, [authors["Ana Neila"]], locations["bebeteca_sala"], "Contação de Histórias").save()
create_activity("Concentração do cortejo", datetime(2023, 6, 14).date(), datetime.strptime("14:00", "%H:%M").time(), 1, [authors["ICAE Umbanda"]], locations["tenda"], "Evento").save()
create_activity("Cortejo", datetime(2023, 6, 14).date(), datetime.strptime("15:00", "%H:%M").time(), 1, [authors["Todos"]], locations["saindo_tenda"], "Desfile").save()
create_activity("Oficinas - Escolas Estaduais", datetime(2023, 6, 14).date(), datetime.strptime("15:00", "%H:%M").time(), 1, [authors["Liduina, Iris, Maurício e Clara"]], locations["tenda"], "Oficina").save()
create_activity("Espetáculo - Palco Bebeteca", datetime(2023, 6, 14).date(), datetime.strptime("15:00", "%H:%M").time(), 1, [authors["Turma do Caracol"]], locations["palco_bebeteca"], "Espetáculo").save()
create_activity("Contação de histórias, brincadeiras e canções - Musicalização para bebês - Bebeteca", datetime(2023, 6, 14).date(), datetime.strptime("15:00", "%H:%M").time(), 0.5, [authors["Priscila Sabino e Amanda Luz"]], locations["bebeteca_sala"], "Atividade Infantil").save()
create_activity("Contação de histórias - Bebeteca", datetime(2023, 6, 14).date(), datetime.strptime("16:30", "%H:%M").time(), 1, [authors["Matrakaberta (Adriana Maciel)"]], locations["bebeteca_sala"], "Contação de Histórias").save()

create_activity("Show Musical", datetime(2023, 6, 14).date(), datetime.strptime("20:30", "%H:%M").time(), 2, [authors["CHIQUITAS & BACANAS"], authors["Angela"]], locations["praca"], "Show").save()
# 15 de Junho
create_activity("Oficina de ilustração + Mesa - Encontro de Ilustradores", datetime(2023, 6, 15).date(), datetime.strptime("09:00", "%H:%M").time(), 3, [authors["André Cerino"], authors["Ilustradores"]], locations["tenda"], "Oficina").save()

create_activity("Leitura, Brincadeiras e Canções - Bebeteca", datetime(2023, 6, 15).date(), datetime.strptime("09:00", "%H:%M").time(), 1, [authors["Tricontando (Ana Neila, Rose Costa e Hozana)"]], locations["palco_bebeteca"], "Atividade Infantil").save()
create_activity("Contação de histórias - Bebeteca", datetime(2023, 6, 15).date(), datetime.strptime("10:20", "%H:%M").time(), 0.67, [authors["Hozana Costa"]], locations["bebeteca_sala"], "Contação de Histórias").save()
create_activity("Espetáculo", datetime(2023, 6, 15).date(), datetime.strptime("10:00", "%H:%M").time(), 1, [authors["Reconito (Liduina com o Grupo Reconito)"]], locations["palco_bebeteca"], "Espetáculo").save()
create_activity("Uris CAUSOS", datetime(2023, 6, 15).date(), datetime.strptime("11:00", "%H:%M").time(), 1, [authors["Eraldo e Angela"]], locations["teatro_pirenopolis"], "Performance").save()
create_activity("Walking Tour", datetime(2023, 6, 15).date(), datetime.strptime("09:00", "%H:%M").time(), 2, [authors["Iris Borges e Sérgio Pompeo"]], locations["caminhada_turistica"], "Passeio").save()
create_activity("Oficina - A Fantástica Matemática", datetime(2023, 6, 15).date(), datetime.strptime("09:00", "%H:%M").time(), 2, [authors["Maria das Dores Brigagão"]], locations["colegio_joaquim_alves"], "Oficina").save()
create_activity("Oficina - A literatura e suas múltiplas possibilidades", datetime(2023, 6, 15).date(), datetime.strptime("09:00", "%H:%M").time(), 2, [authors["Jacqueline de Mattos"]], locations["colegio_joaquim_alves_2"], "Oficina").save()
create_activity("Oficina - Leitura para a Cultura de Paz", datetime(2023, 6, 15).date(), datetime.strptime("09:00", "%H:%M").time(), 2, [authors["Débora Bianca"]], locations["colegio_joaquim_alves_3"], "Oficina").save()
create_activity("Oficina - Mediação de Leitura", datetime(2023, 6, 15).date(), datetime.strptime("09:00", "%H:%M").time(), 2, [authors["Raquel"]], locations["colegio_joaquim_alves_4"], "Oficina").save()


print("Todas as atividades foram inseridas com sucesso.")