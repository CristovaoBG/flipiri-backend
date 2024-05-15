from dataclasses import asdict
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://cristovaobartholo94:307PoKQ0YitxWmGT@cluster0.eisvar1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['flipiri']
collection = db['data']

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
        self._id = ObjectId()
        js = self.to_dict()        
        inserted_id = collection.insert_one(js).inserted_id
        print(f"{inserted_id = }")
        return inserted_id

    def update(self):
        if self._id == -1:
            raise KeyError("Documento não existe.")
        js = self.to_dict()
        modified_count = collection.update_one({js})
        print(f'{modified_count = }')

    def get_child(self, field):
        _id = self.to_dict['field']
        return DataW.from_id(_id)

    @staticmethod
    def from_id(_id: ObjectId, globals_dic):
        doc = collection.find_one(_id)
        _class = globals_dic[doc['_class']]
        instance = _class.__new__(_class)
        del doc['_class']
        instance.__init__(**doc)
        return instance
        
#TODO: apagar debug abaixo
if __name__ == "__main__":
    from autores import *
    # info = Info("João Silva", "Masculino")
    # info.save()
    info = DataW.from_id(ObjectId('6644d002f3a4438f5c50ea3f'), globals())
    print(info)
    print('ok')
        


