from dataclasses import asdict
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from pprint import pprint


DEBUG = True

#TODO: esconder isso aqui pra producao:
uri = "mongodb+srv://cristovaobartholo94:307PoKQ0YitxWmGT@cluster0.eisvar1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
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
        self._id = ObjectId()
        js = self.to_dict()        
        inserted_id = collection.insert_one(js).inserted_id
        print(f"{inserted_id = }")
        return inserted_id

    def update(self):
        if self._id == -1:
            raise KeyError("Documento não existe.")
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
    def get_documents_from_class(class_name):
        docs = collection.find({'_class': class_name})
        output = {}
        for doc in docs:
            # converte os ObjectIds pra string
            for k in doc.keys():
                if k == '_id': continue
                if isinstance(doc[k], ObjectId):
                    doc[k] = doc[k].__repr__()
                # se for lista faz o mesmo dentro da lista
                if isinstance(doc[k], list):
                    doc[k] = [i.__repr__() if isinstance(i, ObjectId) else i for i in doc[k] ]
            # insere no output com a chave _id, removendo ela do valor
            output[str(doc.pop('_id'))] = doc
        return output
    
    @staticmethod
    def get_every_class_name():
        return collection.distinct('_class')
    

#TODO: apagar debug abaixo
if __name__ == "__main__":
    DataW.drop_hole_collecion()
    # test = DataW.get_documents_from_class("Feeding")
    # # pprint(test)
    # print(DataW.get_every_class_name())

        


