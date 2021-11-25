import db
from modelos import *



def Insertar():
    usr = Usuario(descripcion='Informacion Basica', activo=1, edad=20)
    db.session.add(usr)
    db.session.commit()

def Ad_Usuario(des, ed, ac):
    usr = Usuario(descripcion=des, activo=ac, edad=ed)
    db.session.add(usr)
    db.session.commit()
    
def Ad_Comentario(ms, idu):
    cm = Comentario(mensaje=ms, id_u=idu)
    db.session.add(cm)
    db.session.commit()
    
def Cons_Usuarios():
    res = db.session.query(Usuario).all()
    return res


if __name__ == '__main__':
    db.Base.metadata.create_all(db.motor)
    """Insertar()
    cs_usr = db.session.query(Usuario).get(1)
    print(cs_usr.id, cs_usr.activo, cs_usr.edad)"""
    cs_usrexs = db.session.query(Usuario).filter(Usuario.id==1).first()
    Ad_Comentario('Mal partido', cs_usrexs.id)
    print(cs_usrexs.activo)
    print(cs_usrexs.descripcion)
    cs_comentexs = db.session.query(Comentario).filter(Comentario.id_u).all()
    for r in cs_comentexs:
        print(r.id, r.mensaje)

# prueba ssh