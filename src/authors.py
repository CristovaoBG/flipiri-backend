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
class Authors(DataW):
    name: str
    sex: str
    feeding: ObjectId
    _id: ObjectId = -1
