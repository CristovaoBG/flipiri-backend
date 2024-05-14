from dataclasses import asdict, dataclass
from datetime import datetime
from bson import ObjectId

@dataclass
class Feeding:
    from_date: datetime
    to_date: datetime

@dataclass
class Info:
    name: str
    sex: str

@dataclass
class Hosting:
    date_start: datetime
    date_end: datetime
    place: str
    #TODO: preço tb?

@dataclass
class Autores:
    info: ObjectId
    feeding: ObjectId
    activity_list: list[ObjectId]
    hosting: ObjectId
    travel: list[ObjectId]
    
    def to_dict(self):
        return asdict(self)
