from dataclasses import asdict, dataclass
from datetime import datetime
from bson import ObjectId
from wrapper_class import DataW

@dataclass
class Location(DataW):
    name: str
    address: str
    _id: ObjectId = -1
    def simplified_repr(self):
        return (f'{self.name} *')

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
