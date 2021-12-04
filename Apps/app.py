import flask
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'Cultivos'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Cultivos'
mongo = PyMongo(app)

libros = [{'id':0, 'titulo':'Nostradamus'},
            {'id':1, 'titulo':'Python for everybody'}]


@app.route('/')
def inicial():
    return '<h1> Big Data Applications </h1>'


@app.route('/inicio')
def operacion():
    return jsonify(libros)

# http://127.0.0.1:5000/consulta?id=0
@app.route('/consulta', methods=['GET'])
def consulta():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'id no encontrado'
    
    for l in libros:
        if l['id'] == id:
            return jsonify(l)

# http://127.0.0.1:5000/consultadep?dep=RISARALDA
@app.route('/consultadep', methods=['GET'])
def extraer():
    if 'dep' in request.args:
        dpto = request.args['dep']
    else:
        return 'Departamento no encontrado'
    
    col = mongo.db.Cacao
    s = col.find_one({'DEPARTAMENTO':dpto})
    if s:
        salida = {'DEPARTAMENTO': s['DEPARTAMENTO'],
                    'MUNICIPIO': s['MUNICIPIO'],
                    'PERIODO': s['PERIODO'],
                    'AreaSembrada': s['AreaSembrada']}
    else:
        salida = "No encontrado"
    return jsonify({'resultado': salida})


# http://127.0.0.1:5000/consultamun?dep=RISARALDA&mun=PUEBLO RICO
@app.route('/consultamun', methods=['GET'])
def ExtMunicipio():
    if ('dep' in request.args) and ('mun' in request.args):
        dpto = request.args['dep']
        mun = request.args['mun']
    else:
        return 'Departamento no encontrado'
    
    sv = mongo.db.Cacao
    s = sv.find_one({'DEPARTAMENTO':dpto, 'MUNICIPIO': mun})
    if s:
        salida = {'DEPARTAMENTO': s['DEPARTAMENTO'],
                    'MUNICIPIO': s['MUNICIPIO'],
                    'PERIODO': s['PERIODO'],
                    'AreaSembrada': s['AreaSembrada']}
    else:
        salida = "No encontrado"
    return jsonify({'resultado': salida})


# http://127.0.0.1:5000/consultavarios?dep=RISARALDA
@app.route('/consultavarios', methods=['GET'])
def ExtVarios():
    if 'dep' in request.args:
        dpto = request.args['dep']
    else:
        return 'Departamento no encontrado'
    
    sv = mongo.db.Cacao
    consulta = {'DEPARTAMENTO': dpto}
    salida = sv.find(consulta).limit(5)

    if salida:
        return jsonify([{'DEPARTAMENTO': r['DEPARTAMENTO'], 'MUNICIPIO': r['MUNICIPIO']} for r in salida])
    else:
        return 'Departamento no encontrado'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
