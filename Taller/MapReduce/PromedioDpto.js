use Saber11

db.s20201.aggregate([
    {$match: {COLE_CALENDARIO:"B"}},
    {$group: {
        _id:{
            "codigo":"$COLE_COD_DEPTO_UBICACION",
            "ubicacion":"$COLE_DEPTO_UBICACION"},
        promedio: {$avg:"$PUNT_GLOBAL"}}
    },
    {$project: {
        _id:0,
        codigo:"$_id.codigo",
        departamento:"$_id.ubicacion",
        promedio:"$promedio"
    }},
    {$out: 'departamentos'}
])


// export in bash of linux
// mongoexport --db Saber11 --collection departamentos --type=csv --fields codigo,departamento,promedio --out Departamentos.csv
