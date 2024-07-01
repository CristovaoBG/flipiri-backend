from wrapper_class import DataW
from pprint import pprint
from datetime import datetime

def time_interval_to_str(time_1: datetime, time_2: datetime):
    pass

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
            row.append('<hr>'.join(item))
        matrix.append(row)
    y_label = ['author'] + y
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
            row.append('<hr>'.join(item))
        matrix.append(row)
    y_label = ['location'] + y
    dict_list = []
    for row in matrix:
        d = dict(zip(y_label, row))
        dict_list.append(d)
    pprint(dict_list)
    print('ok')
    return dict_list

def trip_by_author():
    authors_data = DataW.get_documents_from_class("Authors")
    #ve todas as atividades que cada um dos autores vai atuar
    trips_data = DataW.get_documents_from_class("Trip")
    auth_and_dates = []
    table = []
    for auth in authors_data.keys():
        trips = []
        auth_name = authors_data[auth]['name']
        for t in trips_data.values():
            for p in t['passenger_list']:
                if str(p) == auth:
                    trips.append(t)
                    break
        trips.sort(key=lambda x:x['date'])
        item = {}
        item['author'] = auth_name
        for i, trip in enumerate(trips):
            item[f'Viagem {i+1}'] = f"{str(trip['date'].day).zfill(2)}/{str(trip['date'].month).zfill(2)} - " \
                                    f"{trip['transportation_type']} " \
                                    f"de {trip['origin']} " \
                                    f"para {trip['destiny']}. " 
        table.append(item)
    # poe rotulo nos restantes
    max_travels = max(list(map(len, table)))
    for r in table:
        i = len(r)
        for j in range(i,max_travels):
            r[f'Viagem {j}'] = ""
    table.sort(key=lambda x:x['author'])
    return table



def get_status(status_key):
    if status_key == "activity_by_author":
        return get_activity_by_author()
    elif status_key == "activity_by_location":
        return get_activity_by_location()
    elif status_key == "trip_by_author":
        return trip_by_author()

if __name__ == "__main__":
    output = get_status("trip_by_author")
    pprint(output)