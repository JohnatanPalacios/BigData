use Saber11

db.s20201.aggregate([
    {$match: {COLE_CALENDARIO:"B"}},
    {$group: {_id:"$COLE_AREA_UBICACION"}},
    {$out: 'area_ubicacion'}
])


// export in bash of linux
// mongoexport --db Saber11 --collection area_ubicacion --type=csv --fields _id --out AreaUbicacion.csv
