var map = function(){
    emit(this.DEPARTAMENTO, this.AreaCosechada);
}

var reduce = function(llave,valor){
    return Array.sum(valor);
}

use Cultivos
db.Cacao.mapReduce(map, reduce, {out:'Area'})
