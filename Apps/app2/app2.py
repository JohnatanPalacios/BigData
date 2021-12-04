# import flask
# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:careloko@localhost:3306/taller1'
# db = SQLAlchemy(app)


# class Departamento(db.Base):
#     __tablename__ = 'departamento'
#     id = db.Column(db.Integer, primary_key=True)
#     dpto = db.Column('departamento', db.Text)
#     municipio = db.relationship('Municipio')


# class Municipio(db.Base):
#     __tablename__ = 'municipio'
#     codane = db.Column('codigo_dane', db.String(20), primary_key=True)
#     mpio = db.Column('municipio', db.Text)
#     id_dpto = db.Column(db.Integer, db.ForeignKey('departamento.id'))
#     incautacion = db.relationship('Incautacion')


# class Incautacion(db.Base):
#     __tablename__ = 'incautacion'
#     id = db.Column(db.Integer, primary_key=True)
#     clasebien = db.Column('clase_bien', db.Text)
#     fecha = db.Column('fecha_hecho', db.Text)
#     cant = db.Column('cantidad', db.Text)
#     cd_mpio = db.Column(db.String(20), db.ForeignKey('municipio.codane'))


# @app.route('/')
# def index():
#     return '<h1>SQL ejemplo</h1>'


# @app.route('/incautacion', methods=['GET'])
# def ConsultaIncautacion():
#     incautaciones = Incautacion.query.get(5)
#     if incautaciones:
#         return jsonify([{'id': i.id} for i in incautaciones])


# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
