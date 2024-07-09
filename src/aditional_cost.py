from bson import ObjectId
from wrapper_class import DataW
from dataclasses import asdict, dataclass

@dataclass
class AditionalCost(DataW):
    name: str
    cost: float = 0.0
    _id: ObjectId = -1

    @staticmethod
    def get_class_header(_, language):
        return {
            'translation': {
                'name': 'Nome',
                'cost': 'Custo'
            },
            'order': ['name', 'cost'],
            'language': 'pt',
            'class_name': 'Custos Adicionais'
        }

    def simplified_repr(self):
        return (f'<i>{self.name}</i>')
    
    def validate(self):
        # verifica se tem um lugar com o mesmo nome
        same_name_list = DataW.get_items_with_field_value('AditionalCost', 'name', self.name)
        if same_name_list:
            if len(same_name_list) > 1 or same_name_list[0]['_id'] != self._id:
                raise ValueError("Já existe um gasto adicional com este nome")
        return super().validate()

                