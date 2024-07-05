from flask import Flask, request, jsonify
from flask_cors import CORS
from wrapper_class import DataW
from pprint import pprint
from utils import str_to_datetime
# TODO: os demais imports deviam estar encapsulados em um arquivo?
from authors import *
from travel import *
from activity import *
from hosting import *
from aditional_cost import *
from category import *
from status import get_status

app = Flask(__name__)
CORS(app)

@app.route('/get_status/', methods=['GET'])
def get_status_request():
    status_label = request.args.get('status_label')
    return jsonify(get_status(status_label))

def save_or_update_data(data_type, data_value, dataW_instance: DataW):
    try:
        if data_type == "new_entry":
            dataW_instance.save()
        else: # edition
            dataW_instance._id = ObjectId(data_value['_id'])
            dataW_instance.update()
    except ValueError as e:
        error_msg = str(e)
        return(jsonify({'success': False, 'error_msg': error_msg}))
    except KeyError as e:
        error_msg = str(e)
        return(jsonify({'success': False, 'error_msg': "ERRO INTERNO: " + error_msg}))
    return(jsonify({'success': True, 'error_msg': "returned no error"}))

@app.route('//add_category//', methods=['POST'])
def add_category():
    data = request.get_json()
    value = data['value']
    new_activity = Category(**value)
    return save_or_update_data(data['type'], value, new_activity)

@app.route('//add_aditional_cost//', methods=['POST'])
def add_aditional_cost():
    data = request.get_json()
    value = data['value']
    new_activity = AditionalCost(**value)
    return save_or_update_data(data['type'], value, new_activity)

@app.route('//add_trip//', methods=['POST'])
def add_trip():
    data = request.get_json()
    value = data['value']
    value['date'] = str_to_datetime(value['date'])
    value['passenger_list'] = [ObjectId(s['_id']) for s in value['passenger_list']]
    new_activity = Trip(**value)
    return save_or_update_data(data['type'], value, new_activity)

@app.route('//add_location//', methods=['POST'])
def add_location():
    data = request.get_json()
    value = data['value']
    new_activity = Location(**value)
    return save_or_update_data(data['type'], value, new_activity)

@app.route('/add_hosting/', methods=['POST'])
def add_hosting():
    data = request.get_json()
    value = data['value']
    new_activity = Hosting(**value)
    return save_or_update_data(data['type'], value, new_activity)

@app.route('/add_author/', methods=['POST'])
def add_author():
    data = request.get_json()
    value = data['value']
    value['arrival'] = str_to_datetime(value['arrival'])
    value['departure'] = str_to_datetime(value['departure'])
    value['hosting'] = ObjectId(value['hosting']['_id'])
    new_activity = Authors(**value)
    return save_or_update_data(data['type'], value, new_activity)

@app.route('/add_activity/', methods=['POST'])
def add_activity():
    data = request.get_json()
    value = data['value']
    # converte Ids
    value['authors'] = [ObjectId(s['_id']) for s in value['authors']]
    value['location'] = ObjectId(value['location']['_id'])
    value['responsible_author'] = ObjectId(value['responsible_author']['_id'])
    # converte datas
    value['date_start'] = str_to_datetime(value['date_start'])
    value['date_end'] = str_to_datetime(value['date_end'])
    value['category'] = ObjectId(value['category']['_id'])
    new_activity = Activity(**value)
    return save_or_update_data(data['type'], data['value'], new_activity)

@app.route('/get_item_from_id/', methods=['GET'])
def get_item_from_id():
    _id = request.args.get('_id')    
    output = DataW.from_id_str(_id, globals()).to_dict()
    DataW.format_to_frontend(output)
    return jsonify(output)

@app.route('/delete_entry/', methods=['POST'])
def delete_item():
    _id = request.get_json().get('_id')
    count = DataW.delete_entry(_id)
    if count != 1:
        return {'success': False, 'error_msg': f"foram feitas {count} alterações."}
    return(jsonify({'success': True, 'error_msg': "returned no error"}))

@app.route('/test/', methods=['GET'])
def get_simplified_representation():
    dataW: DataW = DataW.from_id_str(request.args.get('_id'), globals())
    return dataW.simplified_repr()
    
@app.route('/get_class/', methods=['GET'])
def get_class():
    class_name = request.args.get('class_name')
    print(f"pegando classe: {class_name}")
    output = DataW.get_documents_from_class(class_name)
    return jsonify(DataW.format_to_frontend(output))

@app.route('/get_class_header/', methods=['GET'])
def get_class_header():
    class_name = request.args.get('class_name')
    language = request.args.get('language')
    classe: DataW = globals()[class_name]
    print(f"pegando header daclasse {class_name} em {language}")
    output = classe.get_class_header(classe, language)
    return jsonify(DataW.format_to_frontend(output))

@app.route('/api/', methods=['GET'])
def get_method():
    arg_value = request.args.get('argument_name')    
    print(arg_value)
    return jsonify({'message': f"Funcionando maneiro. arg: {arg_value}"})

@app.route('/api/', methods=['POST'])
def post_method(): 
    data = request.get_json()
    print(data)
    return jsonify({'message': f"Funcionando maneiro. data: {data}"})

@app.route('/get_meal_price/', methods=['GET'])
def get_meal_price():
    _id = request.args.get('_id')    
    price = DataW.get_meal_price()
    data = DataW.format_to_frontend({"price": price})
    return jsonify(data)

@app.route('/set_meal_price/', methods=['POST'])
def set_meal_price():
    data = request.get_json()
    #DataW.get_meal_price()
    print(data)
    DataW.set_meal_price(data['price'])
    return jsonify({'message': f"Funcionando maneiro. data: {data}"})

if __name__ == '__main__':
    app.run(debug=True) 
