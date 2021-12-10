var map = function(){
    if(this.COLE_CALENDARIO=='B'){
        emit(this.COLE_DEPTO_UBICACION,this.PUNT_GLOBAL)
    }
}

var reduce = function(llave,valor){
    return Array.avg(valor)
}

db.s20201.map_reduce(map, reduce, "myresults")