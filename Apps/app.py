import flask
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:careloko@localhost:3306/taller1'
db = SQLAlchemy(app)


class Departamento(db.Model):
    __tablename__ = 'departamento'
    id = db.Column(db.Integer, primary_key=True)
    departamento = db.Column('departamento', db.Text)
    municipio = db.relationship('Municipio')


class Municipio(db.Model):
    __tablename__ = 'municipio'
    codigo_dane = db.Column('codigo_dane', db.String(20), primary_key=True)
    municipio = db.Column('municipio', db.Text)
    id_dpto = db.Column(db.Integer, db.ForeignKey('departamento.id'))
    incautacion = db.relationship('Incautacion')


class Incautacion(db.Model):
    __tablename__ = 'incautacion'
    id = db.Column(db.Integer, primary_key=True)
    clasebien = db.Column('clasebien', db.Text)
    fecha = db.Column('fecha', db.Text)
    cantidad = db.Column('cantidad', db.Text)
    cd_mpio = db.Column(db.String(20), db.ForeignKey('municipio.codigo_dane'))


@app.route('/')
def index():
    return '<h1>SQL ejemplo</h1>'


@app.route('/incautacion', methods=['GET'])
def ConsultaIncautacion():
    incautaciones = Incautacion.query.limit(15).all()
    if incautaciones:
        return jsonify([{'id': i.id} for i in incautaciones])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
