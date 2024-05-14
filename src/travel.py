from dataclasses import asdict, dataclass
from datetime import datetime

@dataclass
class Trip:
    origin: str
    destiny: str
    date: datetime
    transportation_type: str
    price: float
    passenger_list: list[str]
 