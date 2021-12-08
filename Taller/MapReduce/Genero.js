use Saber11

db.s20201.aggregate([
    {$match: {COLE_CALENDARIO:"B"}},
    {$group: {_id:"$COLE_GENERO"}},
    {$out: 'generos'}
])


// export in bash of linux
// mongoexport --db Saber11 --collection generos --type=csv --fields _id --out Generos.csv
