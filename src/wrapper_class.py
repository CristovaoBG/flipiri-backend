from dataclasses import asdict, fields
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from pprint import pprint
from pymongo.errors import OperationFailure
from utils import str_contains_html

DEBUG = True

with open('./key.txt', 'r') as file:
    uri = file.readline().strip()

try:
    client = MongoClient(uri, server_api=ServerApi('1'))
except OperationFailure as e:
    raise OperationFailure("Erro de configuração. A url da chave é válida?")

db = client['flipiri']
collection = db['debug'] if DEBUG else db['data']

class DataW:
    _class: str
    def __post_init__(self):
        self._class = type(self).__name__


    def to_dict(self):
        js = asdict(self)
        js['_id'] = self._id
        js['_class'] = self._class
        return js
    
    def save(self):
        # salva como novo documento
        if self._id != -1:
           raise KeyError("Documento já existe.")
        self.validate()
        self._id = ObjectId()
        js = self.to_dict()        
        inserted_id = collection.insert_one(js).inserted_id
        print(f"{inserted_id = }")
        return inserted_id

    def update(self):
        if self._id == -1:
            raise KeyError("Documento não existe.")
        self.validate()
        js = self.to_dict()
        filter = {'_id': self._id}
        update = {'$set': js}
        modified_count = collection.update_one(filter, update)
        print(f'{modified_count = }')

    def get_child(self, field):
        _id = self.to_dict[field]
        return DataW.from_id(_id)

    def simplified_repr(self):
        return self.to_dict()['_id'].__repr__()

    def validate(self):
        # verifica se tentou injetar html em alguma string dos campos
        for f in fields(self):
            if f.type == str:
                if (str_contains_html(getattr(self, f.name))):
                    raise ValueError("Uso indevido dos caracteres '<' e '>")

    @staticmethod
    def get_class_header(self_class, language):
        # se não tiver implementado no filho
        # apenas cria com o mesmo nome maiúsculo
        keys = [field.name for field in fields(self_class)]
        upp_keys = [s.upper() for s in keys]
        return {
            'translation': {k: uk for k, uk in zip(keys, upp_keys)},
            'order': DataW.get_class_key_order(self_class),
            'language': "None"
            }
    
    @staticmethod
    def get_class_key_order(self_class):
        return sorted([field.name for field in fields(self_class)])

    @staticmethod
    def set_meal_price(price):
        collection.delete_many({"_class": "MealPrice"})
        return collection.insert_one({"_class": "MealPrice", "price": price}).inserted_id
    
    @staticmethod
    def get_meal_price():
        return collection.find_one({"_class": "MealPrice"})['price']

    @staticmethod
    def from_id(_id: ObjectId, globals_dic):
        doc = collection.find_one(_id)
        _class = globals_dic[doc['_class']]
        instance = _class.__new__(_class)
        del doc['_class']
        instance.__init__(**doc)
        return instance
    
    @staticmethod
    def from_id_str(_id: str, globals_dic):
        return DataW.from_id(ObjectId(_id), globals_dic)

    @staticmethod
    def drop_hole_collecion():
        assert DEBUG, "Não se pode dropar uma colection se nao for no modo DEBUG."
        collection.drop()

    @staticmethod
    def get_documents_from_class(class_name, filter = {}) -> dict:
        docs = collection.find({**{'_class': class_name}, **filter})
        output = {}
        for doc in docs:
            # insere no output com a chave _id, removendo ela do valor
            output[str(doc.pop('_id'))] = doc
        return output
    
    @staticmethod
    def get_every_class_name():
        return collection.distinct('_class')
    
    @staticmethod
    def get_items_with_field_value(class_name, field, value):
        docs = list(collection.find({'_class': class_name, field: value}))
        return docs
    
    @staticmethod
    def format_to_frontend(data):
        if isinstance(data, list):
            for id, item in enumerate(data):
                data[id] = DataW.format_to_frontend(item)
        if isinstance(data, dict):
            for key in data.keys():
                data[key]= DataW.format_to_frontend(data[key])
        if isinstance(data, ObjectId):
            return data.__repr__()
        return data

    @staticmethod
    def delete_entry(_id):
        result = collection.delete_one({'_id': ObjectId(_id)})
        return result.deleted_count

#TODO: apagar debug abaixo
if __name__ == "__main__":
    DataW.set_meal_price(10.5)
    print(DataW.get_meal_price())



