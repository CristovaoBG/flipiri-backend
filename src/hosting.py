from dataclasses import dataclass
from datetime import datetime
from bson import ObjectId
from wrapper_class import DataW
from bson import ObjectId

@dataclass
class Hosting(DataW):
    name: str
    vacancies: int = -1
    price: float = 0.0
    _id: ObjectId = -1
    def simplified_repr(self):
        return (f'{self.name} *')
    