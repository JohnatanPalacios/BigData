use Saber11

db.s20201.aggregate([
    {$match: {COLE_CALENDARIO:"B"}},
    {$group: {
        _id:{
            "codane":"$COLE_COD_DANE_SEDE",
			"nombre":"$COLE_NOMBRE_SEDE",
			"departamento":"$COLE_COD_DEPTO_UBICACION",
			"municipio":"$COLE_COD_MCPIO_UBICACION",
			"naturaleza":"$COLE_NATURALEZA",
			"ubicacion":"$COLE_AREA_UBICACION",
			"genero":"$COLE_GENERO"},
		punt_total_lectura:{$avg:"$PUNT_LECTURA_CRITICA"},
		punt_total_matematicas:{$avg:"$PUNT_MATEMATICAS"},
		punt_total_naturales:{$avg:"$PUNT_C_NATURALES"},
		punt_total_sociales:{$avg:"$PUNT_SOCIALES_CIUDADANAS"},
		punt_total_ingles:{$avg:"$PUNT_INGLES"},
		punt_total_global:{$avg:"$PUNT_GLOBAL"}}
    },
    {$project: {
        _id:0,
        codane:"$_id.codane",
		nombre:"$_id.nombre",
		departamento:"$_id.departamento",
		municipio:"$_id.municipio",
		naturaleza:"$_id.naturaleza",
		ubicacion:"$_id.ubicacion",
		genero:"$_id.genero",
		punt_total_lectura:"$punt_total_lectura",
		punt_total_matematicas:"$punt_total_matematicas",
		punt_total_naturales:"$punt_total_naturales",
		punt_total_sociales:"$punt_total_sociales",
		punt_total_ingles:"$punt_total_ingles",
		punt_total_global:"$punt_total_global"
    }},
    {$out: 'colegios'}
])


// export in bash of linux
// mongoexport --db Saber11 --collection colegios --type=csv --fields codane,nombre,departamento,municipio,naturaleza,ubicacion,genero,punt_total_lectura,punt_total_matematicas,punt_total_naturales,punt_total_sociales,punt_total_ingles,punt_total_global --out Colegios.csv
