select `Nom communes équipées` ,count(*) as Nb_Station from `velib-data-project-483613.data_velib.velib`  where `Station en fonctionnement` = 'OUI' GROUP BY `Nom communes équipées`;

select `Nom station` from `velib-data-project-483613.data_velib.velib`  where `Retour vélib possible` = 'OUI' ;
