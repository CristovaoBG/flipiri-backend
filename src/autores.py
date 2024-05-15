from dataclasses import dataclass
from datetime import datetime
from bson import ObjectId
from wrapper_class import DataW
from bson import ObjectId


@dataclass
class Feeding(DataW):
    from_date: datetime
    to_date: datetime
    _id: ObjectId = -1

@dataclass
class Info(DataW):
    name: str
    sex: str
    _id: ObjectId = -1

@dataclass
class Hosting(DataW):
    date_start: datetime
    date_end: datetime
    place: str
    #TODO: preço tb?
    _id: ObjectId = -1

@dataclass
class Autores(DataW):
    info: ObjectId
    feeding: ObjectId
    activity_list: list[ObjectId]
    hosting: ObjectId
    travel: list[ObjectId]
    _id: ObjectId = -1
