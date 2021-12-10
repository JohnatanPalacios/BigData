use Saber11

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
// mongoexport --db Saber11 --collection estudiantes --type=csv --fields colegio,punt_lectura,punt_matematicas,punt_naturales,punt_sociales,punt_ingles,punt_global --out Estudiantes.csv
