from dataclasses import dataclass
from datetime import datetime
from bson import ObjectId
from wrapper_class import DataW
from bson import ObjectId
from utils import datetimes_have_intersection


@dataclass
class Feeding(DataW):
    from_date: datetime
    to_date: datetime
    _id: ObjectId = -1
    def simplified_repr(self):
        dt = self.to_date - self.from_date
        dt_days = dt.days
        return (f'Alimentação para {dt_days} dias *')


@dataclass
class Authors(DataW):
    name: str
    sex: str
    feeding: ObjectId
    _id: ObjectId = -1

    def simplified_repr(self):
        return (f'{self.name} *')

    def get_author_activities_ids(self) ->list[str]:
        docs = DataW.get_documents_from_class("Activity")
        # otimizavel
        # return [id for id, activity in docs.items() if self._id in activity['authors']]
        output = []
        for id, activity in docs.items(): 
            print(activity['authors'])
            # tem que converter pra string por algum motivo
            if str(self._id) in [act.split('\'')[1] for act in activity['authors']]:
                output.append(id)
        return output
                

    def is_free_between(self, time_start: datetime, time_end: datetime):
        # pega as proprias atividades
        activity_id_list = self.get_author_activities_ids()
        # pega instancia das atividades
        from activity import Activity
        activity_list: list[Activity] = []

        for i, ac in enumerate(activity_id_list): 
            # obs: lista compreensiva estraga o 'locals()'
            activity_list.append(DataW.from_id_str(ac, locals()))
            
        is_free = True
        for activity in activity_list:
            if datetimes_have_intersection( time_start,
                                            time_end,
                                            activity.date_start,
                                            activity.date_end):
                is_free = False
                break
        return is_free
