from dataclasses import dataclass
from datetime import datetime
from bson import ObjectId
from wrapper_class import DataW
from bson import ObjectId
from utils import datetimes_have_intersection


# @dataclass
# class Feeding(DataW):
#     from_date: datetime
#     to_date: datetime
#     _id: ObjectId = -1
#     def simplified_repr(self):
#         dt = self.to_date - self.from_date
#         dt_days = dt.days
#         return (f'Alimentação para {dt_days} dias *')


@dataclass
class Authors(DataW): #TODO: pq plural?
    name: str
    sex: str
    # feeding: ObjectId
    hosting: ObjectId
    arrival: datetime
    departure: datetime
    _id: ObjectId = -1

    def simplified_repr(self):
        return (f'{self.name} *')

    def get_author_activities_ids(self) ->list[str]:
        docs = DataW.get_documents_from_class("Activity")
        output = []
        for id, activity in docs.items(): 
            print(activity['authors'])
            if self._id in activity['authors']:
                output.append(id)
        return output

    def is_free_between(self, time_start: datetime, time_end: datetime, ignore: ObjectId):
        # pega as proprias atividades
        activity_id_list = self.get_author_activities_ids()
        # pega instancia das atividades
        from activity import Activity
        activity_list: list[Activity] = []
        # obs: lista compreensiva estraga o 'locals()'
        for i, ac in enumerate(activity_id_list):     
            activity_list.append(DataW.from_id_str(ac, locals()))
        is_free = True
        for activity in activity_list:
            if activity._id == ignore: continue
            if datetimes_have_intersection( time_start,
                                            time_end,
                                            activity.date_start,
                                            activity.date_end):
                is_free = False
        return is_free

    def validate(self):
        if self.departure < self.arrival:
            raise ValueError("Erro de datas. A data de chegada deve ser "
                            " anterior a data de partida.")
        # verifica se tem um lugar com o mesmo nome
        same_name_list = DataW.get_items_with_field_value('Authors', 'name', self.name)
        if same_name_list:
            if len(same_name_list) > 1 or same_name_list[0]['_id'] != self._id:
                raise ValueError(f"Já existe um autor com o nome '{self.name}'" )
        return super().validate()
            