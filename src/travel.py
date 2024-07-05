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

    @staticmethod
    def get_class_header(_, language):
        return {
            'translation': {
                'origin': 'Origem',
                'destiny': 'Destino',
                'date': 'Data',
                'transportation_type': 'Tipo de Transporte',
                'price': 'Preço',
                'passenger_list': 'Lista de Passageiros'
            },
            'order': ['origin', 'destiny', 'date', 'transportation_type', 'price', 'passenger_list'],
            'language': "pt",
        }

    def validate(self):
        if not self.passenger_list:
            raise ValueError("Não há nenhum passageiro incluso na viagem.")
        return super().validate()
        
 