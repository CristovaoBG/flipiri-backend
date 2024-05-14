from dataclasses import asdict, dataclass
from datetime import datetime
from typing import List
from activity import Activity
from travel import Trip

@dataclass
class Feeding:
    from_date: datetime
    to_date: datetime

@dataclass
class Info:
    name: str
    sex: str


@dataclass
class Hosting:
    date_start: datetime
    date_end: datetime
    place: str
    #TODO: preço tb?

@dataclass
class Autores:
    info: Info
    feeding: Feeding
    activity_list: list[Activity]
    hosting: Hosting
    travel: list[Trip]
    
    def to_dict(self):
        return asdict(self)
