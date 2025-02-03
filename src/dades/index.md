---
title: L'activitat
toc: true
---

```js
const dictionary = FileAttachment("./font/dictionary.json").json();
```

# Fonts i dades

## Eficiència energètica
La **font principal** son les dades corresponents a la informació pública dels **certificats d’eficiència energètica dels edificis** proveïdes per l'[Institut Català d’Energia (ICAEN)](https://icaen.gencat.cat/ca/inici/).

Podeu accedir a les dades:

- Al [**repositori**](https://github.com/fndvit/mds-udg-viz-i-dgpcd-hackathon-25/blob/main/src/dades/font/certificats.csv), un `CSV` amb informació adicional.
- A la pàgina de *Certificats d’eficiència energètica d’edificis* al [**portal de dades obertes**](https://analisi.transparenciacatalunya.cat/Energia/Certificats-d-efici-ncia-energ-tica-d-edificis/j6ii-t3w2).
- Mitjançant l'[**API**](https://dev.socrata.com/foundry/analisi.transparenciacatalunya.cat/j6ii-t3w2).

El conjunt de dades té un total de **1,34 millions de fileres**, cadescuna amb **69 columnes**.

A sota trobareu la descripció de cada columna, agafada de la font original:

```js
Inputs.table(
  dictionary,
  { rows: 15,
    columns: ["Nom de columna", "Descripció", "Tipus de dades"],
    width: {
      "Nom de columna":180,
       "Tipus de dades": 120,
    }
  })
```

Per simplificar una possible tasca d'agregació per **àrees geogràfiques**, hem afegit a cada certificat l'identificador de l'àrea més petita per a la que tenim dades sociodemogrèfiques, la secció censal (`MUNDISSEC`):

```js
Inputs.table([
  {
    "Nom de columna": "mundissec",
    "Descripció": "Identificador únic de la secció censal on es troba l'edifici",
    "Tipus de dades": "Text"
  }
],
  {
    width: {
      "Nom de columna":180,
       "Tipus de dades": 120,
    }
  }
)
```
---
## Renda
Com a **font secundária** us recomanem les dades de l'*Atlas de Distribució de la Renda a les Llars* (ADRH en espanyol) de l'Institut Nacional d'Estatística (INE), que proporciona informació sobre el nivell i la distribució de renda desglossada segons variables demogràfiques bàsiques de la població a nivell territorial molt detallat.

Podeu accedir a les [**taules**](https://www.ine.es/dynt3/inebase/es/index.htm?padre=12385&capsel=12384) a la pàgina de l'INE.

Les variables d'estudi incloses a l'ADRH son:

- Indicadors de renda mitjana i mitjana
- Distribució per font d'ingressos
- Percentatge de població amb ingressos per unitat de consum per sota de determinats llindars fixos per sexe
- Percentatge de població amb ingressos per unitat de consum per sota determinats llindars fixos per sexe i trams d'edat
- Percentatge de població amb ingressos per unitat de consum per sota de determinats llindars fixos per sexe i nacionalitat
- Percentatge de població amb ingressos per unitat de consum per sota/dessus de determinats llindars relatius per sexe
- Percentatge de població amb ingressos per unitat de consum per sota/dessus de determinats llindars relatius per sexe i trams d'edat
- Percentatge de població amb ingressos per unitat de consum per sota/dessus de determinats llindars relatius per sexe i nacionalitat
- Índex de Gini i distribució de la renda P80/P20
- Indicadors demogràfics

---

## Arxius geogràfics
Com ja hem mencionat, hem afegit l'identificador de la secció censal a les dades de cada certificat —de cada edifici— doncs no necessiteu geocodificar les dades. I ja n'hi ha una capa a Mapbox si voleu fer mapes interactius com s'explica a les qüestions tècniques.

Si tot i aixó en voleu aquests arxius geogràfics, les trobareu a l'[**Institut Cartogràfic i Geològic de Catalunya** (ICGC)](https://www.icgc.cat/ca/Geoinformacio-i-mapes/Dades-i-productes/Geoinformacio-cartografica/Seccions-censals).