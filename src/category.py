from dataclasses import dataclass
from bson import ObjectId
from wrapper_class import DataW

@dataclass
class Category(DataW):
    name: str
    price: float = 0.0
    _id: ObjectId = -1

    @staticmethod
    def get_class_header(_, language):
        return {
            'translation': {'name': 'Nome', 'price': 'Preço'},
            'order': ['name', 'price'],
            'language': 'pt',
            'class_name': 'Categorias'
        }

    def simplified_repr(self):
        return (f'<i>{self.name}</i>')

    def validate(self):
        same_name_list = DataW.get_items_with_field_value('Category', 'name', self.name)
        if same_name_list:
            if len(same_name_list) > 1 or same_name_list[0]['_id'] != self._id:
                raise ValueError(f"Já existe um autor com o nome '{self.name}'" )
        return super().validate()