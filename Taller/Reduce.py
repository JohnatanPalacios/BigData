# cat ./csv/Colegios.csv | python3 Map.py | python3 Reduce.py

import sys
from Models import db
from Models.Methods import *
db.Base.metadata.create_all(db.motor)

mpios = []
coles = []

for line in sys.stdin:
    line = line.strip()
    codane,cole,dpto,mpio,nat,ubi,gen,pl,pm,pn,ps,pi,pg = line.split('\t')
    if (codane and cole and dpto and mpio and nat and ubi
        and gen and pl and pm and pn and ps and pi and pg):
        pl = round(float(pl), 2)
        pm = round(float(pm), 2)
        pn = round(float(pn), 2)
        ps = round(float(ps), 2)
        pi = round(float(pi), 2)
        pg = round(float(pg), 2)
        
        if mpio not in mpios:
            mpios.append(mpio)
            Add_Mpio(mpio)
        if cole not in coles:
            coles.append(cole)
            Add_Colegio(codane,cole,dpto,mpio,nat,ubi,gen)
        Add_Est(pl,pm,pn,ps,pi,pg,cole)
