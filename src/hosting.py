from dataclasses import dataclass
from datetime import datetime
from bson import ObjectId
from wrapper_class import DataW
from bson import ObjectId

@dataclass
class Hosting(DataW):
    date_start: datetime
    date_end: datetime
    place: str
    guest_list: list[ObjectId]
    vacancies: int = -1
    price: float = 0.0
    _id: ObjectId = -1
