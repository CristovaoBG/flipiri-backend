import wrapper_class
from authors import *
from travel import *
from activity import *
from hosting import *
from datetime import datetime

wrapper_class.DEBUG = True

# Criando hospedagem genérica
id_hosting = Hosting("Local Padrão", 1, 0.0).save()

# Criando autores (mantido como estava)
autores = {
    "Bebeteca": Authors("Bebeteca", "Desconhecido", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Ana Neila": Authors("Ana Neila", "Feminino", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Hozana Costa": Authors("Hozana Costa", "Feminino", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Grupo Reconto": Authors("Grupo Reconto", "Grupo", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Eraldo e Angela": Authors("Eraldo e Angela", "Grupo", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Iris Borges": Authors("Iris Borges", "Feminino", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Sergio Pompeu": Authors("Sergio Pompeu", "Masculino", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Maria das Dores": Authors("Maria das Dores", "Feminino", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Brigagão": Authors("Brigagão", "Desconhecido", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Jacqueline de Mattos": Authors("Jacqueline de Mattos", "Feminino", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Débora Bianca": Authors("Débora Bianca", "Feminino", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Raquel": Authors("Raquel", "Feminino", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Maria Amélia": Authors("Maria Amélia", "Feminino", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "SANEAGO": Authors("SANEAGO", "Grupo", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Marcia Lages": Authors("Marcia Lages", "Feminino", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Matrakaberta": Authors("Matrakaberta", "Grupo", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Turma do Caracol": Authors("Turma do Caracol", "Grupo", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Maria": Authors("Maria", "Feminino", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "André Carino": Authors("André Carino", "Masculino", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Angela B. Café": Authors("Angela B. Café", "Feminino", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save(),
    "Marcelo Barra": Authors("Marcelo Barra", "Masculino", id_hosting, datetime(1,1,1), datetime(9999,1,1)).save()
}

# Criando locais (mantido como estava)
locais = {
    "Tenda": Location("Tenda", "Local do evento").save(),
    "Tenda B": Location("Tenda B", "Local do evento - área alternativa").save(),
    "Palco": Location("Palco - Centro de Artes e Música Ita e Alaor", "Local do evento").save(),
    "Bebeteca sala": Location("Bebeteca sala - Centro de Artes e Música Ita e Alaor", "Local do evento").save(),
    "Teatro": Location("Teatro de Pirenópolis", "Local do evento").save(),
    "Colégio Sala 1": Location("Colégio Comendador Joaquim Alves - Sala 1", "Local do evento").save(),
    "Colégio Sala 2": Location("Colégio Comendador Joaquim Alves - Sala 2", "Local do evento").save(),
    "Colégio Sala 3": Location("Colégio Comendador Joaquim Alves - Sala 3", "Local do evento").save(),
    "Colégio Sala 4": Location("Colégio Comendador Joaquim Alves - Sala 4", "Local do evento").save(),
    "Praça": Location("Praça", "Local do evento").save(),
    "Praça B": Location("Praça B", "Local do evento - área alternativa").save()
}

# Criando atividades (atualizado com as datas corretas)
atividades = [
    Activity("Leitura, Brincadeiras e Canções", datetime(2024, 6, 12, 9, 0), datetime(2024, 6, 12, 10, 0), [autores["Bebeteca"]], autores["Bebeteca"], locais["Tenda"], 0, 100, "Infantil"),
    Activity("Tricontando", datetime(2024, 6, 12, 9, 0), datetime(2024, 6, 12, 10, 0), [autores["Ana Neila"], autores["Hozana Costa"]], autores["Ana Neila"], locais["Palco"], 0, 100, "Infantil"),
    Activity("Contação de histórias", datetime(2024, 6, 12, 10, 0), datetime(2024, 6, 12, 10, 30), [autores["Bebeteca"]], autores["Bebeteca"], locais["Bebeteca sala"], 0, 100, "Infantil"),
    Activity("Espetáculo", datetime(2024, 6, 12, 10, 0), datetime(2024, 6, 12, 11, 0), [autores["Grupo Reconto"]], autores["Grupo Reconto"], locais["Palco"], 0, 100, "Infantil"),
    Activity("Uns CAUSOS", datetime(2024, 6, 12, 11, 0), datetime(2024, 6, 12, 12, 0), [autores["Eraldo e Angela"]], autores["Eraldo e Angela"], locais["Teatro"], 0, 100, "Geral"),
    Activity("Walking Tour", datetime(2024, 6, 12, 9, 0), datetime(2024, 6, 12, 11, 0), [autores["Iris Borges"], autores["Sergio Pompeu"]], autores["Iris Borges"], locais["Tenda B"], 0, 100, "Turismo"),
    Activity("Oficina - A Fantástica Matemática", datetime(2024, 6, 12, 9, 0), datetime(2024, 6, 12, 11, 0), [autores["Maria das Dores"], autores["Brigagão"]], autores["Maria das Dores"], locais["Colégio Sala 1"], 0, 100, "Educação"),
    Activity("Oficina - A literatura e suas múltiplas possibilidades", datetime(2024, 6, 12, 9, 0), datetime(2024, 6, 12, 11, 0), [autores["Jacqueline de Mattos"]], autores["Jacqueline de Mattos"], locais["Colégio Sala 2"], 0, 100, "Literatura"),
    Activity("Oficina - Leitura para a Cultura de Paz", datetime(2024, 6, 12, 9, 0), datetime(2024, 6, 12, 11, 0), [autores["Débora Bianca"]], autores["Débora Bianca"], locais["Colégio Sala 3"], 0, 100, "Educação"),
    Activity("Oficina - Mediação de Leitura", datetime(2024, 6, 12, 9, 0), datetime(2024, 6, 12, 11, 0), [autores["Raquel"]], autores["Raquel"], locais["Colégio Sala 4"], 0, 100, "Literatura"),
    Activity("Mesa", datetime(2024, 6, 12, 11, 0), datetime(2024, 6, 12, 12, 0), [autores["Maria Amélia"]], autores["Maria Amélia"], locais["Palco"], 0, 100, "Debate"),
    Activity("Espetáculo - Teatro Infantil", datetime(2024, 6, 12, 11, 30), datetime(2024, 6, 12, 12, 30), [autores["SANEAGO"]], autores["SANEAGO"], locais["Praça"], 0, 100, "Teatro"),
    Activity("Roda de conversa", datetime(2024, 6, 12, 14, 0), datetime(2024, 6, 12, 15, 0), [autores["Marcia Lages"]], autores["Marcia Lages"], locais["Teatro"], 0, 100, "Debate"),
    Activity("Espetáculo", datetime(2024, 6, 12, 15, 0), datetime(2024, 6, 12, 16, 0), [autores["Matrakaberta"]], autores["Matrakaberta"], locais["Palco"], 0, 100, "Teatro"),
    Activity("Contação de histórias", datetime(2024, 6, 12, 15, 0), datetime(2024, 6, 12, 15, 30), [autores["Hozana Costa"]], autores["Hozana Costa"], locais["Bebeteca sala"], 0, 100, "Infantil"),
    Activity("Contação de histórias", datetime(2024, 6, 12, 15, 30), datetime(2024, 6, 12, 16, 0), [autores["Jacqueline de Mattos"]], autores["Jacqueline de Mattos"], locais["Bebeteca sala"], 0, 100, "Infantil"),
    Activity("Show - Bebeteca", datetime(2024, 6, 12, 16, 30), datetime(2024, 6, 12, 17, 30), [autores["Turma do Caracol"], autores["Maria"], autores["André Carino"]], autores["Turma do Caracol"], locais["Palco"], 0, 100, "Infantil"),
    Activity("Mesa de debates: O livro das Nossas Vidas", datetime(2024, 6, 12, 17, 0), datetime(2024, 6, 12, 18, 0), [autores["Iris Borges"]], autores["Iris Borges"], locais["Teatro"], 0, 100, "Debate"),
    Activity("Show de Talentos", datetime(2024, 6, 12, 17, 0), datetime(2024, 6, 12, 20, 0), [autores["Angela B. Café"]], autores["Angela B. Café"], locais["Praça"], 0, 100, "Música"),
    Activity("Cerimônia de Encerramento", datetime(2024, 6, 15, 20, 30), datetime(2024, 6, 15, 21, 30), [autores["Marcelo Barra"]], autores["Marcelo Barra"], locais["Praça B"], 0, 100, "Encerramento")
]

# Salvando as atividades
for atividade in atividades:
    atividade.save()

print("Dados inseridos com sucesso!")