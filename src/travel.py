from dataclasses import asdict, dataclass
from datetime import datetime
from wrapper_class import DataW
from bson import ObjectId


@dataclass
class Trip(DataW):
    origin: str
    destiny: str
    date: datetime
    transportation_type: str
    price: float
    passenger_list: list[ObjectId]
    _id: ObjectId = -1
 