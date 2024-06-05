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

app = Flask(__name__)
CORS(app)

@app.route('/add_author/', methods=['POST'])
def post_author_data():
    data = request.get_json()
    # converte Ids
    data['authors'] = [ObjectId(s['_id']) for s in data['authors']]
    data['location'] = ObjectId(data['location']['_id'])
    data['responsible_author'] = ObjectId(data['responsible_author']['_id'])
    # converte datas
    data['date_start'] = str_to_datetime(data['date_start'])
    data['date_end'] = str_to_datetime(data['date_end'])
    new_activity = Activity(**data)
    try:
        new_activity.save()
    except KeyError as e:
        error_msg = str(e)
        return(jsonify({'success': False, 'error_msg': error_msg}))
    return(jsonify({'success': True, 'error_msg': "returned no error"}))


@app.route('/test/', methods=['GET'])
def get_simplified_representation():
    dataW = DataW.from_id_str(request.args.get('_id'), globals())
    return dataW.simplified_repr()
    
@app.route('/get_class/', methods=['GET'])
def get_class():
    class_name = request.args.get('class_name')
    print(f"pegando classe: {class_name}")
    return jsonify(DataW.get_documents_from_class(class_name))

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

if __name__ == '__main__':
    app.run(debug=True) 
