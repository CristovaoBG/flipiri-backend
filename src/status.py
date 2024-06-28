from wrapper_class import DataW
from pprint import pprint
from prettytable import PrettyTable

def get_activity_by_author():
    authors_data = DataW.get_documents_from_class("Authors")
    #ve todas as atividades que cada um dos autores vai atuar
    activities_data = DataW.get_documents_from_class("Activity")
    auth_and_dates = []
    for id in activities_data.keys():
        for auth in activities_data[id]['authors']:
            entry = {}
            entry['auth_id'] = auth
            entry['date'] = activities_data[id]['date_start']
            entry['date_str'] = str(activities_data[id]['date_start'])[:10]
            entry['act_name'] = activities_data[id]['name']
            # entry['loc'] = activities_data[id]['location']
            hours, _, _ = map(int, str(activities_data[id]['date_start'])[10:].split(':'))
            entry['period'] = "MANHA" if hours < 12 else ("TARDE" if hours < 6 else "NOITE")
            entry['y_value'] = f"{entry['date_str']} - {entry['period']}"
            auth_and_dates.append(entry)
    auth_and_dates.sort(key = lambda x : x['date'])
    # varre todos os x e y
    x = []
    y = []
    for e in auth_and_dates:
        x.append(e['auth_id'])
        y.append(e['y_value'])
    x.sort(key=lambda x:authors_data[str(x)]['name'])
    # remove duplicados
    x = list(dict.fromkeys(x))
    y = list(dict.fromkeys(y))
    # varre criando a matriz
    matrix = []
    for i in x:
        row = [authors_data[str(i)]['name']]
        for j in y:
            item = []
            for aad in auth_and_dates:
                if (aad['auth_id'] == i and
                    aad['y_value'] == j
                    ):
                    item.append(aad['act_name'])
            row.append(' & '.join(item))
        matrix.append(row)
                
    y_label = ['author'] + y
    tabela = PrettyTable()
    tabela.field_names = y_label
    # Adicionar linhas
    for i in matrix:
        tabela.add_row(i)
    with open("output.txt", 'w') as arquivo:
        arquivo.write(str(tabela))
    # coloca no formato de lista de dicionarios
    dict_list = []
    for row in matrix:
        d = dict(zip(y_label, row))
        dict_list.append(d)
    pprint(dict_list)
    print('ok')
    return dict_list
    
        
def get_activity_by_location():
    locations_data = DataW.get_documents_from_class("Location")
    #ve todas as atividades que cada um dos autores vai atuar
    activities_data = DataW.get_documents_from_class("Activity")
    auth_and_dates = []
    for id in activities_data.keys():
        loc = activities_data[id]['location']
        entry = {}
        entry['loc_id'] = loc
        entry['date'] = activities_data[id]['date_start']
        entry['date_str'] = str(activities_data[id]['date_start'])[:10]
        entry['act_name'] = activities_data[id]['name']
        # entry['loc'] = activities_data[id]['location']
        hours, _, _ = map(int, str(activities_data[id]['date_start'])[10:].split(':'))
        entry['period'] = "MANHA" if hours < 12 else ("TARDE" if hours < 6 else "NOITE")
        entry['y_value'] = f"{entry['date_str']} - {entry['period']}"
        auth_and_dates.append(entry)
    auth_and_dates.sort(key = lambda x : x['date'])
    # varre todos os x e y
    x = []
    y = []
    for e in auth_and_dates:
        x.append(e['loc_id'])
        y.append(e['y_value'])
    x.sort(key=lambda x:locations_data[str(x)]['name'])
    # remove duplicados
    x = list(dict.fromkeys(x))
    y = list(dict.fromkeys(y))
    # varre criando a matriz
    matrix = []
    for i in x:
        row = [locations_data[str(i)]['name']]
        for j in y:
            item = []
            for aad in auth_and_dates:
                if (aad['loc_id'] == i and
                    aad['y_value'] == j
                    ):
                    item.append(aad['act_name'])
            row.append(' & '.join(item))
        matrix.append(row)
                
    y_label = ['location'] + y
    dict_list = []
    for row in matrix:
        d = dict(zip(y_label, row))
        dict_list.append(d)
    pprint(dict_list)
    print('ok')
    return dict_list




def get_status(status_key):
    if status_key == "activity_by_author":
        return get_activity_by_author()
    elif status_key == "activity_by_location":
        return get_activity_by_location()

if __name__ == "__main__":
    get_status("atividade_por_autor")