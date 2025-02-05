# Quines zones geogràfiques tenen el major potencial per a la producció d'energia renovable i l'autosuficiència?

Per respondre a la nostra pregunta, usarem els següents datasets:

## Dataset dels certificats d'eficiència energètica dels edificis

Sobre aquest primer dataset, proveït per l'ICAEN (l'Institut Català d'Energia), usarem principalment els següents atributs: 
- **D'identificació geogràfica** per agrupar per zones, com per exemple poblacio, comarca o provincia.
- **D'infraestructura d'energia renovable**, per veure on ja hi ha instal·lacions. Usarem variables com per exemple *solar_fotovoltaica*, *solar_termica*, *energia_geotermica* o *sistema_biomassa*.
- **D'eficiència i consum energètic**, com *qualificaci_de_consum_d*, *energia_prim_ria_no_renovable* o *consum_d_energia_final*.
- **Factors climàtics**, com *zona_climatic*.
- **El tipus d'edifici**, anomenat com *us_edifici* al dataset.

## Dataset de dades metereològiques 

Per saber les zones geogràfiques amb major potencial per a la producció d'energia renovable, volem saber les zones de catalunya on, per exemple, hi tenim més **precipitacions**, més **vent** o més **irradiància solar**. D'aquesta manera sabrem si hi ha millors zones que d'altres per fer-hi instal·lacions de panells solars, centrals hidroelèctriques o centrals eòliques (tinguent en compte la viabilitat d'aquestes instal·lacions).
Dit això, hem creat un nou dataset ajuntant-ne 3 de diferents, que son els següents (extrets del portal de dades obertes de la Generalitat):

- Primer tenim el dataset de [**Dades meteorològiques registrades a totes les estacions de la Xarxa d'Estacions Meteorològiques Automàtiques (XEMA)**](https://analisi.transparenciacatalunya.cat/Medi-Ambient/Dades-meteorol-giques-de-la-XEMA/nzvn-apee/data) del Servei Meteorològic de Catalunya (METEOCAT). Aquest dataset conté variables mesurades amb una freqüència inferior a la diària, generalment semi-horària.

- Llavors hem obtingut el dataset que conté les [**Metadades associades a cadascuna de les estacions de la XEMA**](https://analisi.transparenciacatalunya.cat/Medi-Ambient/Metadades-estacions-meteorol-giques-autom-tiques/yqwd-vj5e/data) (Xarxa d'Estacions Meteorològiques Automàtiques), integrada a la Xarxa d'Equipaments Meteorològics de la Generalitat de Catalunya (Xemec), del Servei Meteorològic de Catalunya. Cada estació s'identifica amb un codi.

- I per últim, el dataset que conté les [**Metadades de les variables meteorològiques**](https://analisi.transparenciacatalunya.cat/Medi-Ambient/Metadades-variables-meteorol-giques/4fb2-n3yi/data), que conté les metadades associades a cadascuna de les variables de la Xarxa d'Estacions Meteorològiques Automàtiques (XEMA). Cada variable s'identifica amb un codi i representen les diferents variables que es poden llegir a les diferents estacions (com per exemple precipitacions, temperatura, humitat, etc).


## Dataset de dades demogràfiques

Per ajudar a respondre a la pregunta de l'autosuficiència, hem obtingut [**dades demogràfiques**](https://www.idescat.cat/indicadors/?id=aec&n=15228) per veure la demanda energètica, amb el número d'habitants per les diferents poblacions de Catalunya. Aquest dataset l'obtenim de l'[**IDESCAT**](https://www.idescat.cat/) (Institut d'Estadística de Catalunya).

També ens pot interessar classificar aquests valors per sexe, raça, edat o altres característiques. En aquest cas usarem datasets que proporciona l'INE (Institut Nacional d'Estadística) sobre [**estadístiques del Padró continu**](https://www.ine.es/dynt3/inebase/index.htm?padre=6232) per cada població de Catalunya.
