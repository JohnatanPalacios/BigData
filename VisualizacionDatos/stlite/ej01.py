# from bson.code import Code
# map = Code ("function(){emit(this.DEPARTAMENTO,1)}")
# reduce = Code ("function(llave,valor){return Array.sum(valor)}")
# result = db.Cacao.map_reduce(map, reduce, "Dptos")

import streamlit as st
from pymongo import *
import pandas as pd


client = MongoClient('mongodb://localhost:27017/')
db = client['Cultivos']

cursor = db.Dptos.find()
dptos = [d['_id'] for d in cursor]


st.title('Cacao')
dpto = st.sidebar.selectbox('Departamentos: ', dptos)
data = db.Cacao.find_one({"DEPARTAMENTO": dpto})
st.write(data)
