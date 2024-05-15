from dataclasses import asdict, dataclass
from datetime import datetime
from bson import ObjectId
from wrapper_class import DataW

@dataclass
class Cerimonialist(DataW):
    name: str
    price: float
    _id: ObjectId = -1

@dataclass
class fix_price(DataW):
    cost_name: str
    price: float
    _id: ObjectId = -1

@dataclass
class Festival(DataW):
    cerimonialists: list[ObjectId]
    authors: list[ObjectId]
    total_price: float
    _id: ObjectId = -1
