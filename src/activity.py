from dataclasses import asdict, dataclass
from datetime import datetime
from bson import ObjectId
from wrapper_class import DataW

@dataclass
class AgeRange(DataW):
    age_start: int
    age_end: int
    _id: ObjectId = -1

@dataclass
class Location(DataW):
    name: str
    address: str
    _id: ObjectId = -1

@dataclass
class Activity(DataW):
    name: str
    date: datetime
    duration: datetime
    authors: list[ObjectId]
    responsible_author: int
    location: ObjectId
    age_range: ObjectId
    category: str
    _id: ObjectId = -1
