from dataclasses import asdict, dataclass
from datetime import datetime
from bson import ObjectId
from wrapper_class import DataW
from utils import datetimes_have_intersection

@dataclass
class Location(DataW):
    name: str
    address: str
    _id: ObjectId = -1

    def simplified_repr(self):
        return (f'{self.name} *')
    
    def validate(self):
        print("validating loc")

    def is_free_between(self, time_start: datetime, time_end: datetime):
        # pega as proprias atividades
        activity_id_list =  DataW.get_documents_from_class("Activity",{"location": self._id})
        # pega instancia das atividades
        activity_list: list[Activity] = []
        for ac in activity_id_list: 
            # obs: lista compreensiva estraga o 'locals()'
            activity_list.append(DataW.from_id_str(ac, globals()))
        is_free = True
        for activity in activity_list:
            if datetimes_have_intersection( time_start,
                                            time_end,
                                            activity.date_start,
                                            activity.date_end):
                is_free = False
                break
        return is_free

@dataclass
class Activity(DataW):
    name: str
    date_start: datetime
    date_end: datetime
    authors: list[ObjectId]
    responsible_author: int
    location: ObjectId
    age_range_start: int
    age_range_end: int
    category: str
    _id: ObjectId = -1

    def simplified_repr(self):
        return (f'{self.name} *')
    
    def validate(self):
        # raise KeyError("erro")
        if self.date_start > self.date_end:
            raise ValueError("Horários incorretos, "
                            "o fim do evento aconteceria antes de seu início.")
        elif self.date_start == self.date_end:
            raise ValueError("Horários incorretos, o tempo "
                            "de duração do evento é nulo.")
        # verifica se horário do autor ta vago
        # varre todos as atividades dos autores envolvidos pra ver colisoes
        from authors import Authors
        for auth_id in self.authors:
            auth: Authors = DataW.from_id(auth_id, locals())
            if not auth.is_free_between(self.date_start, self.date_end):
                raise ValueError(f"O participante \"{auth.name}\" "
                                "não está disponível nesse período")
        # TODO: deveria validar do autor responsavel tb?
        # valida local
        loc :Location = DataW.from_id(self.location, globals())
        # loc.validate()
        if (not loc.is_free_between(self.date_start, self.date_end)):
            raise ValueError(f"O local \"{loc.name}\" "
                             "não estará vago nesse período")

    