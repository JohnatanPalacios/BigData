var map = function(){
    if(this.DEPARTAMENTO == 'RISARALDA'){
        emit(this.MUNICIPIO, this.AreaCosechada);
    }
}

var reduce = function(llave,valor){
    return Array.sum(valor);
}

use Cultivos
db.Cacao.mapReduce(map, reduce, {out:'AreaRisaralda'})
