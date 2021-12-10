import flask
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:careloko@localhost:3306/taller2'
db = SQLAlchemy(app)


class Departamento(db.Model):
    __tablename__ = 'departamento'
    id = db.Column(db.Integer, primary_key=True)
    departamento = db.Column('departamento', db.Text)
    promedio = db.Column('promedio', db.Float)


@app.route('/')
def index():
    return '<h1>Consultar Departamentos y su Promedio</h1>'


@app.route('/departamentos', methods=['GET'])
def ConsultaDptos():
    dptos = Departamento.query.limit(15).all()
    if dptos:
        return jsonify([{'Departamento': d.departamento,
                        'Promedio': d.promedio} for d in dptos])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
