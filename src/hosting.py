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

    @staticmethod
    def get_class_header(_, language):
        return {
            'translation': {
                'name': 'Nome',
                'vacancies': 'Vagas',
                'price': 'Preço'
            },
            'order': ['name', 'vacancies', 'price'],
            'language': 'pt',
            'class_name': 'Hospedagem'
        }

    def simplified_repr(self):
        return (f'<i>{self.name}</i>')

    def validate(self):
        same_name_list = DataW.get_items_with_field_value('Hosting', 'name', self.name)
        if same_name_list:
            if len(same_name_list) > 1 or same_name_list[0]['_id'] != self._id:
                raise ValueError("Já existe uma hospedagem com este nome")
        return super().validate()
    