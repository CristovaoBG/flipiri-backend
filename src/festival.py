from dataclasses import asdict, dataclass
from datetime import datetime
from bson import ObjectId

@dataclass
class Cerimonialist:
    name: str
    price: float

@dataclass
class fix_price:
    cost_name: str
    price: float

@dataclass
class Festival:
    cerimonialists: list[ObjectId]
    authors: list[ObjectId]
    total_price: float = -1.0

