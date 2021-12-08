use Saber11

db.createCollection("counter")
db.counter.insert({_id: "nameID", seq: 0});
function nextVal(name) {
    var ret = db.counter.findAndModify(
        {
            query: { _id: name },
            update: { $inc: { seq: 1 } },
            new: true
        });
    return ret.seq;
 };

db.s20201.aggregate([
    {$match: {COLE_CALENDARIO:"B"}},
    {$group: {
        _id:{
            colegio:"$COLE_NOMBRE_SEDE",
            punt_lectura:"$PUNT_LECTURA_CRITICA",
            punt_matematicas:"$PUNT_MATEMATICAS",
            punt_naturales:"$PUNT_C_NATURALES",
            punt_sociales:"$PUNT_SOCIALES_CIUDADANAS",
            punt_ingles:"$PUNT_INGLES",
            punt_global:"$PUNT_GLOBAL"}}
    },
    {$project: {
        _id:0,
        colegio:"$_id.colegio",
        punt_lectura:"$_id.punt_lectura",
        punt_matematicas:"$_id.punt_matematicas",
        punt_naturales:"$_id.punt_naturales",
        punt_sociales:"$_id.punt_sociales",
        punt_ingles:"$_id.punt_ingles",
        punt_global:"$_id.punt_global"
    }},
    {$out: 'estudiantes'}
])


// export in bash of linux
// mongoexport --db Saber11 --collection departamentos --type=csv --fields codigo,ubicacion,promedio --out Departamentos.csv

// var map = function(){
//     if(this.COLE_CALENDARIO == "B"){
//         emit({
//             nombre:nextVal("nameID"),
//             colegio:this.COLE_NOMBRE_SEDE,
//             punt_lectura:this.PUNT_LECTURA_CRITICA,
//             punt_matematicas:this.PUNT_MATEMATICAS,
//             punt_naturales:this.PUNT_C_NATURALES,
//             punt_sociales:this.PUNT_SOCIALES_CIUDADANAS,
//             punt_ingles:this.PUNT_INGLES,
//             punt_global:this.PUNT_GLOBAL},
//             1);
//     }
// };
// var reduce = function(key,value){
//  return Array.sum(value);
// };

db.s20201.mapReduce(map,reduce,{out: "estudiantes"})