from wrapper_class import DataW
from pprint import pprint
from datetime import datetime
from authors import *
from activity import *
from utils import date_to_str_simple, time_to_str_simple

def money_to_str(v):
    s = f"R$ {v:,.2f}"
    return s.replace(",", "v").replace(".", ",").replace("v", ".")

def get_activity_by_author():
    authors_data = DataW.get_documents_from_class("Authors")
    #ve todas as atividades que cada um dos autores vai atuar
    activities_data = DataW.get_documents_from_class("Activity")
    location_data = DataW.get_documents_from_class("Location")
    auth_and_dates = []
    for id in activities_data.keys():
        for auth in activities_data[id]['authors']:
            entry = {}
            entry['auth_id'] = auth
            entry['date'] = activities_data[id]['date_start']
            entry['date_str'] = str(activities_data[id]['date_start'])[:10]
            hours, minutes, _ = map(int, str(activities_data[id]['date_start'])[10:].split(':'))
            hours_end, minutes_end, _ = map(int, str(activities_data[id]['date_end'])[10:].split(':'))
            location_name = location_data[str(activities_data[id]['location'])]['name']
            entry['act_name'] = f"<strong>{activities_data[id]['name']}</strong>" \
                f" ({hours}h{minutes if minutes != 0 else ''}-" \
                f"{hours_end}h{minutes_end if minutes_end != 0 else ''})" \
                f"<br><small><small>{location_name}</small></small>"
            # entry['loc'] = activities_data[id]['location']
            entry['period'] = "MANHA" if hours < 12 else ("TARDE" if hours < 18 else "NOITE")
            entry['y_value'] = f"{entry['date_str'].replace('-','/')} - {entry['period']}"
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
            row.append('<hr color=\"#383838\">'.join(item))
        matrix.append(row)
    y_label = ['Autor'] + y
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
        hours, minutes, _ = map(int, str(activities_data[id]['date_start'])[10:].split(':'))
        hours_end, minutes_end, _ = map(int, str(activities_data[id]['date_end'])[10:].split(':'))
        entry['act_name'] = f"<strong>{activities_data[id]['name']}</strong>" \
                f" ({hours}h{minutes if minutes != 0 else ''}-" \
                f"{hours_end}h{minutes_end if minutes_end != 0 else ''})" \
        # entry['loc'] = activities_data[id]['location']
        entry['period'] = "MANHA" if hours < 12 else ("TARDE" if hours < 18 else "NOITE")
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
            row.append('<hr color=\"#383838\">'.join(item))
        matrix.append(row)
    y_label = ['Localização'] + y
    dict_list = []
    for row in matrix:
        d = dict(zip(y_label, row))
        dict_list.append(d)
    pprint(dict_list)
    print('ok')
    return dict_list

def author_details():
    authors_data = DataW.get_documents_from_class("Authors")
    activities_data = DataW.get_documents_from_class("Activity")
    category_data = DataW.get_documents_from_class("Category")
    #ve todas as atividades que cada um dos autores vai atuar
    trips_data = DataW.get_documents_from_class("Trip")
    table = []
    for auth in authors_data.keys():
        author_object: Authors = DataW.from_id_str(auth, globals())
        # Viagens
        trips = []
        auth_name = authors_data[auth]['name']
        for t in trips_data.values():
            for p in t['passenger_list']:
                if str(p) == auth:
                    trips.append(t)
                    break
        trips.sort(key=lambda x:x['date'])
        item = []
        for trip in trips:
            item.append(f"{trip['transportation_type']} " \
                        f"de {trip['origin']} " \
                        f"para {trip['destiny']}. " \
                        f"<br><small>{date_to_str_simple(trip['date'])}</small>")
        tripsStr = "<hr color=\"#383838\">".join(item)
        # Atividades
        auth_activities = []
        for act in activities_data:
            if auth in list(map(str,activities_data[act]['authors'])):
                auth_activities.append(activities_data[act])
        auth_activities_str = []
        for act in auth_activities:
            date = date_to_str_simple(act['date_start'])
            time = time_to_str_simple(act['date_start'])
            s = f"{act['name']}<br><small>({date} - {time})</small>"
            auth_activities_str.append(s)
        # Chegada e partida
        arrival = author_object.arrival
        departure = author_object.departure
        # Add na tabela
        table.append(
            {
            'Autor': auth_name,
            'Viagens': tripsStr, 
            'Refeições': author_object.count_meals(),
            'Pernoites': author_object.count_overnights(),
            'Atividades': "<hr color=\"#383838\">".join(auth_activities_str),
            'Chegada / Partida': f"{date_to_str_simple(arrival)}"
                     f"<hr color=\"#383838\">"
                     f"{date_to_str_simple(departure)}"
            })
    table.sort(key=lambda x:x['Autor'])
    return table

def total_costs():
    activities_data = DataW.get_documents_from_class("Activity")
    categories_data = DataW.get_documents_from_class("Category")
    trips_data = DataW.get_documents_from_class("Trip")
    authors_data = DataW.get_documents_from_class("Authors")
    hosting_data = DataW.get_documents_from_class("Hosting")
    # pega custos adicionais
    aditional_costs = DataW.get_documents_from_class("AditionalCost")
    table_aditional_costs = [
        {
            'Nome': ac['name'],
            'Custo': ac['cost']
        }
        for ac in aditional_costs.values()
    ]
    # gasto com atividades
    # varre todas as atividades, olha o preco da categoria 
    ac_values = activities_data.values()
    categories_counter = {category: 0 for category in categories_data.keys()}
    category_table = []
    for category_id in categories_data.keys():
        name = categories_data[category_id]['name']
        price = categories_data[category_id]['price']
        price_str = money_to_str(price)
        acts = [ac for ac in ac_values if str(ac['category']) == category_id]
        involved_people = []
        for people in [p_list['authors'] for p_list in acts]:
            for p in people:
                involved_people.append(p)
        categories_counter[category_id] += len(involved_people)
        category_table.append({
            'Nome': f"Eventos da categoria \"{name}\"<br>"
                    f"<small><small>{price_str} "
                    f"para {len(involved_people)} "
                    f"envolvidos</small></small>",
            'Custo': len(involved_people)*price
        })
    # viagens
    trips_price = sum([t['price'] for t in trips_data.values()])
    table_trips = [{'Nome': 'Viagens', 'Custo': trips_price}]
    # hospedagem
    hosting_cost = 0
    for auth in authors_data.values():
        overnight_cost = hosting_data[str(auth['hosting'])]['price']
        overnights = auth['departure'].day - auth['arrival'].day
        hosting_cost += overnight_cost * overnights
    hosting_table = [{
        'Nome': 'Hospedagens',
        'Custo': hosting_cost
    }]
    # alimentacao
    authors: list[Authors] = []
    for auth in authors_data.keys():
        authors.append(DataW.from_id_str(auth, globals()))
    meal_counter = 0
    for auth in authors:
        meal_counter += auth.count_meals()
    meal_table = [{
        'Nome': f"Alimentação<br>"
                f"<small><small>"
                f"{meal_counter} alimentação para {len(authors)} "
                f"participantes</small></small>",
        'Custo': meal_counter * DataW.get_meal_price()
    }]
    # organiza, une e soma
    table_aditional_costs.sort(key=lambda x:x['Nome'])
    category_table.sort(key=lambda x:x['Nome'])
    table_union = (
        table_aditional_costs
        + category_table
        + table_trips
        + hosting_table
        + meal_table
    )
    total_costs = 0
    for entry in table_union:
        total_costs += entry['Custo']
        entry['Custo'] = money_to_str(entry['Custo'])
    table_union.append({
        'Nome': '<big><strong>TOTAL</strong></big>',
        'Custo': f'<big><strong>{money_to_str(total_costs)}</strong></big>'
    })
    return table_union

def activity_costs():
    activities_data = DataW.get_documents_from_class("Activity")
    categories_data = DataW.get_documents_from_class("Category")
    authors_data = DataW.get_documents_from_class("Authors")

    table = []
    total = 0
    for act in activities_data.values():
        # pega custo da categoria
        cat_id = str(act['category'])
        # auth_list = act['authors']
        auth_names = [authors_data[str(a)]['name'] for a in act['authors']]
        cat_name = categories_data[cat_id]['name']
        cat_price = categories_data[cat_id]['price']
        subtotal = len(auth_names) * cat_price
        total += subtotal
        table.append({
            'Nome': act['name'],
            'Categoria': f'{cat_name}<br><small><small>{money_to_str(cat_price)} / participante</small></small>',
            # 'value per author': money_to_str(cat_price),
            'Autores': ",<br>".join(auth_names),
            'Subtotal': money_to_str(subtotal)
        })
    table.append({
        'Nome': '<big><strong>TOTAL:</strong></big>',
        'categoria': '-',
        'Valor por autor': '-',
        'autores': '-',
        'Subtotal': f'<big><strong>{money_to_str(total)}</strong></big>'
})
    return table

def get_status(status_key):
    if status_key == "activity_by_author":
        return get_activity_by_author()
    elif status_key == "activity_by_location":
        return get_activity_by_location()
    elif status_key == "author_details":
        return author_details()
    elif status_key == "total_costs":
        return total_costs()
    elif status_key == "activity_costs":
        return activity_costs()
    
if __name__ == "__main__":
    output = get_status("total_costs")
    pprint(output)