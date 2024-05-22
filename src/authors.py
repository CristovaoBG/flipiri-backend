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
    def simplified_repr(self):
        dt = self.to_date - self.from_date
        dt_days = dt.days
        return (f'Alimentação para {dt_days} dias *')


@dataclass
class Authors(DataW):
    name: str
    sex: str
    feeding: ObjectId
    _id: ObjectId = -1
    def simplified_repr(self):
        return (f'{self.name} *')
