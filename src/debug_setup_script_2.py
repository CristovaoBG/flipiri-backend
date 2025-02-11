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
id_debate = Category("Debate", 500.0).save()
id_teatro = Category("Teatro", 500.0).save()
id_evento = Category("Evento", 500.0).save()

# Criação de locais
id_praca = Location("Praça / Zazá Café", "Praça Central").save()
id_teatro_ = Location("Teatro de Pirenópolis", "Centro da Cidade").save()
id_teatro2 = Location("Teatro de Pirenópolis 2", "Centro da Cidade").save()
id_palco = Location("Palco - Centro de Artes e Música Itá", "Centro Cultural").save()
id_palco2 = Location("Palco 2 - Centro de Artes e Música Itá", "Centro Cultural").save()
id_tenda = Location("Tenda", "Área de Eventos").save()
id_tenda2 = Location("Tenda 2", "Área de Eventos").save()
id_pousada = Location("Pousada Stª Bárbara", "Rua Principal").save()
id_espaco = Location("Teatro de Pirenópolis ou Espaço", "Centro da Cidade").save()
id_igreja = Location("Palco da Igreja", "Igreja Central").save()
id_musica = Location("Música Itá e Alaor", "Centro Cultural").save()
id_musica2 = Location("Música Itá e Alaor 2", "Centro Cultural").save()
id_auditorio = Location("Auditório do Centro de Artes e Música Itá", "Centro Cultural").save()
id_saida = Location("Saindo da Tenda", "Área de Eventos").save()
id_caminhada = Location("Caminhada aos pontos turísticos", "Centro Histórico").save()
id_colegio = Location("Colégio Comendador Joaquim Alves", "Rua da Educação").save()
id_colegio2 = Location("Colégio Comendador Joaquim Alves - Sala 2", "Rua da Educação").save()
id_colegio3 = Location("Colégio Comendador Joaquim Alves - Sala 3", "Rua da Educação").save()
id_colegio4 = Location("Colégio Comendador Joaquim Alves - Sala 4", "Rua da Educação").save()
id_bebeteca = Location("Bebeteca sala - Centro de Artes e Música Itá e Alaor", "Centro Cultural").save()

id_hosting = Hosting("Pousada padrão", 100, 50.0).save()

# Criação de autores (simplificado, sem hospedagem)
autores = {}
for nome in [
                "Rafael Correa",
                "Beto Seabra",
                "Mauricio", 
                "Clara Arreguy", 
                "Fabrício Gomes", 
                "Luz Marina", 
                "Rose Costa", 
                "Célia", 
                "Reconto", 
                "Priscila Sabino",
                "Amanda Luz", 
                "Iris Borges", 
                "Mediadora: Lariza Amélia Eloi", 
                "Ana Neila", 
                "ICAE Comunidade", 
                "Liduina Bartholo", 
                "Turma do Caracol", 
                "Débora Bianca", 
                "Matrakaberta (Adriana Maciel)",
                "CHIQUITAS & BACANAS",
                "Angela",
                "André Cerino",
                "Hozana Costa",
                "Eraldo", 
                "Sérgio Pompeo",
                "Maria das Dores Brigagão",
                "Jacqueline de Mattos",
                "Raquel", 
                "Maria Amélia", 
                "SANEAGO", 
                "Marcia Lages",  
                "Angela B. Café", 
                "Marcelo Barra"
             ]:
    autores[nome] = Authors(nome, "Não especificado", id_hosting, datetime(year=2023,month=6,day=12), datetime(year=2023,month=6,day=16)).save()

# Criação de atividades
# 12 de Junho
Activity("Rafael Correa / Lançamento de livros", datetime(2023, 6, 12, 20, 0), datetime(2023, 6, 12, 22, 0), [autores["Rafael Correa"]], autores["Rafael Correa"], id_praca, 0, 100, id_teatro).save()

# 13 de Junho
Activity("Mesa de Debates: O que os Livros me Ensinaram", datetime(2023, 6, 13, 11, 0), datetime(2023, 6, 13, 13, 0), [autores["Beto Seabra"]], autores["Beto Seabra"], id_teatro_, 0, 100, id_debate).save()
Activity("Mesa Russos", datetime(2023, 6, 13, 11, 0), datetime(2023, 6, 13, 13, 0), [autores["Mauricio"]], autores["Mauricio"], id_palco, 0, 100, id_debate).save()
Activity("Mesa de Debates: O que os Livros trazem de Goiás", datetime(2023, 6, 13, 16, 0), datetime(2023, 6, 13, 18, 0), [autores["Clara Arreguy"]], autores["Clara Arreguy"], id_palco, 0, 100, id_debate).save()
Activity("Lançamento de livro", datetime(2023, 6, 13, 17, 0), datetime(2023, 6, 13, 19, 0), [autores["Fabrício Gomes"]], autores["Fabrício Gomes"], id_tenda, 0, 100, id_evento).save()
Activity("Cerimônia de Abertura", datetime(2023, 6, 13, 19, 0), datetime(2023, 6, 13, 20, 0), [autores["Fabrício Gomes"]], autores["Fabrício Gomes"], id_pousada, 0, 100, id_evento).save()

# 14 de Junho
Activity("Trupe dos Cirandeiros", datetime(2023, 6, 14, 8, 0), datetime(2023, 6, 14, 22, 0), [autores["Luz Marina"]], autores["Luz Marina"], id_espaco, 0, 100, id_teatro).save()
Activity("Pina literária", datetime(2023, 6, 14, 10, 0), datetime(2023, 6, 14, 11, 0), [autores["Rose Costa"]], autores["Rose Costa"], id_igreja, 0, 100, id_evento).save()
Activity("Espetáculo", datetime(2023, 6, 14, 9, 30), datetime(2023, 6, 14, 10, 30), [autores["Célia"]], autores["Célia"], id_musica, 0, 100, id_teatro).save()
Activity("Espetáculo", datetime(2023, 6, 14, 10, 0), datetime(2023, 6, 14, 11, 0), [autores["Reconto"]], autores["Reconto"], id_musica2, 0, 100, id_teatro).save()
Activity("Musicalização", datetime(2023, 6, 14, 10, 0), datetime(2023, 6, 14, 10, 30), [autores["Priscila Sabino"], autores["Amanda Luz"]], autores["Priscila Sabino"], id_bebeteca, 0, 5, id_evento).save()
Activity("Contação de histórias para bebês", datetime(2023, 6, 14, 10, 30), datetime(2023, 6, 14, 11, 0), [autores["Iris Borges"]], autores["Iris Borges"], id_bebeteca, 0, 5, id_itinerancia).save()
Activity("Mesa de Debates: Literatura e Ascensão Social", datetime(2023, 6, 14, 11, 0), datetime(2023, 6, 14, 13, 0), [autores["Mediadora: Lariza Amélia Eloi"]], autores["Mediadora: Lariza Amélia Eloi"], id_auditorio, 0, 100, id_debate).save()
Activity("Contação de histórias - Bebeteca", datetime(2023, 6, 14, 11, 0), datetime(2023, 6, 14, 11, 30), [autores["Ana Neila"]], autores["Ana Neila"], id_bebeteca, 0, 12, id_itinerancia).save()
Activity("Concentração do cortejo", datetime(2023, 6, 14, 14, 0), datetime(2023, 6, 14, 15, 0), [autores["ICAE Comunidade"]], autores["ICAE Comunidade"], id_tenda, 0, 100, id_evento).save()
Activity("Cortejo", datetime(2023, 6, 14, 15, 0), datetime(2023, 6, 14, 16, 0), [autores["ICAE Comunidade"]], autores["ICAE Comunidade"], id_saida, 0, 100, id_evento).save()
Activity("Oficinas: Escolas Estaduais", datetime(2023, 6, 14, 15, 0), datetime(2023, 6, 14, 16, 0), [autores["Liduina Bartholo"], autores["Iris Borges"], autores["Mauricio"], autores["Clara Arreguy"]], autores["Iris Borges"], id_tenda, 0, 100, id_evento).save()
Activity("Contação de histórias, brincadeiras e canções - Bebeteca", datetime(2023, 6, 14, 15, 0), datetime(2023, 6, 14, 16, 0), [autores["Débora Bianca"]], autores["Débora Bianca"], id_musica, 0, 5, id_evento).save()
Activity("Musicalização para bebês - Bebeteca", datetime(2023, 6, 14, 15, 0), datetime(2023, 6, 14, 16, 20), [autores["Priscila Sabino"], autores["Amanda Luz"]], autores["Amanda Luz"], id_bebeteca, 0, 5, id_teatro).save()
Activity("Contação de histórias - Bebeteca", datetime(2023, 6, 14, 16, 30), datetime(2023, 6, 14, 17, 30), [autores["Matrakaberta (Adriana Maciel)"]], autores["Matrakaberta (Adriana Maciel)"], id_palco, 0, 12, id_teatro).save()
Activity("Show Musical", datetime(2023, 6, 14, 20, 30), datetime(2023, 6, 14, 22, 30), [autores["CHIQUITAS & BACANAS"], autores["Angela"]], autores["CHIQUITAS & BACANAS"], id_praca, 0, 100, id_evento).save()

# 15 de Junho
Activity("Oficina de ilustração + Mesa - Encontro de Ilustradores", datetime(2023, 6, 15, 9, 0), datetime(2023, 6, 15, 12, 0), [autores["André Cerino"]], autores["André Cerino"], id_tenda2, 0, 100, id_evento).save()
Activity("Leitura, Brincadeiras e Canções - Bebeteca", datetime(2023, 6, 15, 9, 0), datetime(2023, 6, 15, 10, 0), [autores["Ana Neila"], autores["Rose Costa"], autores["Hozana Costa"]], autores["Rose Costa"], id_palco, 0, 5, id_evento).save()
Activity("Contação de histórias - Bebeteca", datetime(2023, 6, 15, 10, 20), datetime(2023, 6, 15, 11, 0), [autores["Hozana Costa"]], autores["Hozana Costa"], id_bebeteca, 0, 5, id_itinerancia).save()
Activity("Espetáculo", datetime(2023, 6, 15, 10, 0), datetime(2023, 6, 15, 11, 0), [autores["Reconto"], autores["Liduina Bartholo"]], autores["Reconto"], id_palco, 0, 5, id_teatro).save()
Activity("Uns CAUSOS", datetime(2023, 6, 15, 11, 0), datetime(2023, 6, 15, 12, 0), [autores["Eraldo"], autores["Angela"]], autores["Angela"], id_teatro_, 0, 100, id_teatro).save()
Activity("Walking Tour", datetime(2023, 6, 15, 9, 0), datetime(2023, 6, 15, 11, 0), [autores["Iris Borges"], autores["Sérgio Pompeo"]], autores["Iris Borges"], id_caminhada, 0, 100, id_evento).save()
Activity("Oficina - A Fantástica Matemática", datetime(2023, 6, 15, 9, 0), datetime(2023, 6, 15, 11, 0), [autores["Maria das Dores Brigagão"]], autores["Maria das Dores Brigagão"], id_colegio, 0, 100, id_evento).save()
Activity("Oficina - A literatura e suas múltiplas possibilidades", datetime(2023, 6, 15, 9, 0), datetime(2023, 6, 15, 11, 0), [autores["Jacqueline de Mattos"]], autores["Jacqueline de Mattos"], id_colegio2, 0, 100, id_evento).save()
Activity("Oficina - Leitura para a Cultura de Paz", datetime(2023, 6, 15, 9, 0), datetime(2023, 6, 15, 11, 0), [autores["Débora Bianca"]], autores["Débora Bianca"], id_colegio3, 0, 100, id_evento).save()
Activity("Oficina - Mediação de Leitura", datetime(2023, 6, 15, 9, 0), datetime(2023, 6, 15, 11, 0), [autores["Raquel"]], autores["Raquel"], id_colegio4, 0, 100, id_evento).save()
Activity("Mesa", datetime(2023, 6, 15, 11, 0), datetime(2023, 6, 15, 13, 0), [autores["Maria Amélia"]], autores["Maria Amélia"], id_palco, 0, 100, id_debate).save()
Activity("Espetáculo - Teatro Infantil", datetime(2023, 6, 15, 11, 30), datetime(2023, 6, 15, 12, 30), [autores["SANEAGO"]], autores["SANEAGO"], id_praca, 0, 12, id_teatro).save()
Activity("Roda de conversa", datetime(2023, 6, 15, 14, 30), datetime(2023, 6, 15, 16, 30), [autores["Marcia Lages"]], autores["Marcia Lages"], id_teatro_, 0, 100, id_debate).save()
Activity("Espetáculo - Bebeteca", datetime(2023, 6, 15, 15, 0), datetime(2023, 6, 15, 16, 0), [autores["Matrakaberta (Adriana Maciel)"]], autores["Matrakaberta (Adriana Maciel)"], id_palco, 0, 5, id_teatro).save()
Activity("Contação de histórias - Bebeteca", datetime(2023, 6, 15, 15, 0), datetime(2023, 6, 15, 15, 30), [autores["Hozana Costa"]], autores["Hozana Costa"], id_bebeteca, 0, 5, id_itinerancia).save()
Activity("Contação de histórias - Bebeteca", datetime(2023, 6, 15, 15, 30), datetime(2023, 6, 15, 16, 0), [autores["Jacqueline de Mattos"]], autores["Jacqueline de Mattos"], id_bebeteca, 0, 5, id_itinerancia).save()
Activity("Show - Bebeteca", datetime(2023, 6, 15, 16, 30), datetime(2023, 6, 15, 17, 30), [autores["Turma do Caracol"]], autores["Turma do Caracol"], id_palco, 0, 5, id_evento).save()
Activity("Mesa de debates: o livro das Nossas Vidas", datetime(2023, 6, 15, 16, 0), datetime(2023, 6, 15, 18, 0), [autores["Mediadora: Lariza Amélia Eloi"]], autores["Mediadora: Lariza Amélia Eloi"], id_teatro2, 0, 100, id_debate).save()
Activity("Show de Talentos", datetime(2023, 6, 15, 17, 0), datetime(2023, 6, 15, 20, 0), [autores["Angela B. Café"]], autores["Angela B. Café"], id_praca, 0, 100, id_evento).save()
Activity("Cerimônia de Encerramento", datetime(2023, 6, 15, 20, 30), datetime(2023, 6, 15, 22, 30), [autores["Marcelo Barra"]], autores["Marcelo Barra"], id_praca, 0, 100, id_evento).save()

id_trip1 = Trip("brasilia", "piri", datetime(2025, 6, 1), "aviao", 10.0, [autores["Turma do Caracol"]]).save()
id_trip1 = Trip("piri", "brasilia", datetime(2025, 6, 10), "aviao", 10.0, [autores["Turma do Caracol"]]).save()
id_trip1 = Trip("brasilia", "groenlândia", datetime(2025, 6, 11), "aviao", 10.0, [autores["Turma do Caracol"]]).save()
id_trip1 = Trip("brasilia", "piri", datetime(2025, 6, 1), "carro", 10.0, [autores["Clara Arreguy"],autores["Fabrício Gomes"],]).save()
id_trip1 = Trip("piri", "brasilia", datetime(2025, 6, 10), "carro", 10.0, [autores["Clara Arreguy"],autores["Fabrício Gomes"],autores["Rose Costa"]]).save()


AditionalCost("ABERTURA", 1000.0).save()
AditionalCost("CACHÊ MÚSICOS / SARAU", 1200.0).save()
AditionalCost("COMPRA DE LIVROS PARA ESCOLAS", 50000.0).save()
AditionalCost("SITE GUTO", 3000.0).save()
AditionalCost("JÚNIOR ARTES DAS PEÇAS", 2000.0).save()
AditionalCost("SINALIZAÇÃO VISUAL", 3000.0).save()
AditionalCost("OFICINAS", 8400.0).save()
AditionalCost("MESAS", 9000.0).save()
AditionalCost("BEBETECAS", 7700.0).save()
AditionalCost("SONORIZAÇÃO SANTA BÁRBARA", 2500.0).save()
AditionalCost("SONORIZAÇÃO DO CINEMA OU TEATRO", 4500.0).save()
AditionalCost("TRANSMISSÃO DE", 3000.0).save()
AditionalCost("PRODUÇÃO DE FOTO", 8000.0).save()
AditionalCost("FOTÓGRAFO ITINERÂNCIA CAMPO", 500.0).save()
AditionalCost("INTÉRPRETE DE LIBRAS", 3000.0).save()
AditionalCost("CLIMATIZADOR CINEMA", 1200.0).save()
AditionalCost("LIMPEZA", 1000.0).save()
AditionalCost("RECEPÇÃO", 1600.0).save()
AditionalCost("LOCAÇÃO DE CADEIRAS", 500.0).save()
AditionalCost("IMPOSTO ICA", 3160.0).save()

DataW.set_meal_price(10.5)

print("ok")