from dataclasses import asdict, dataclass
from datetime import datetime
from travel import Travel

@dataclass
class Age_range:
    age_start: int
    age_end: int

@dataclass
class Location:
    name: str
    address: str

@dataclass
class Activity:
    name: str
    date: datetime
    duration: datetime
    authors: list[int]
    responsible_author: int
    location: Location
    age_range: Age_range
    category: str
