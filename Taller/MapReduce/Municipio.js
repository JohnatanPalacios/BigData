use Saber11

db.s20201.aggregate([
    {$match: {COLE_CALENDARIO:"B"}},
    {$group:
        {_id:
            {
            "codigo":"$COLE_COD_MCPIO_UBICACION",
            "ubicacion":"$COLE_MCPIO_UBICACION"}
    }},
    {$project: {
        _id:0,
        codigo:"$_id.codigo",
        municipio:"$_id.ubicacion",
    }},
    {$out: 'municipios'}
])


// export in bash of linux
// mongoexport --db Saber11 --collection municipios --type=csv --fields codigo,municipio --out Municipios.csv
