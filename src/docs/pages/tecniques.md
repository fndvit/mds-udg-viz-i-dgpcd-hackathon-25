---
title: Exemples de codi
toc: true
---

<style>
  img {
    border-radius: 1rem;
    box-shadow: 0 0 1rem rgba(0,0,0,0.15);
    max-width: 42rem;
    width: 100%;
    transition: all 0.3s;
  }
  img:hover {
    opacity:.7;
  }
</style>

```js
import chroma from "npm:chroma-js";
 
const dadesAtur = [
  { year: 2000, Barcelona: 10, Girona: 8, Lleida: 7, Tarragona: 9 },
  { year: 2001, Barcelona: 9, Girona: 7.5, Lleida: 6.8, Tarragona: 8.5 },
  { year: 2002, Barcelona: 8.5, Girona: 7.2, Lleida: 6.6, Tarragona: 8.2 },
  { year: 2003, Barcelona: 8.2, Girona: 7, Lleida: 6.3, Tarragona: 8 },
  { year: 2004, Barcelona: 8, Girona: 6.8, Lleida: 6, Tarragona: 7.8 },
  { year: 2005, Barcelona: 7.8, Girona: 6.6, Lleida: 5.8, Tarragona: 7.6 },
  { year: 2006, Barcelona: 7.5, Girona: 6.3, Lleida: 5.6, Tarragona: 7.3 },
  { year: 2007, Barcelona: 7.2, Girona: 6, Lleida: 5.4, Tarragona: 7 },
  { year: 2008, Barcelona: 7, Girona: 5.8, Lleida: 5.2, Tarragona: 6.8 },
  { year: 2009, Barcelona: 9, Girona: 7.5, Lleida: 6.8, Tarragona: 8.5 },
  { year: 2010, Barcelona: 9.5, Girona: 7.8, Lleida: 7, Tarragona: 8.8 },
  { year: 2011, Barcelona: 10, Girona: 8, Lleida: 7.2, Tarragona: 9 },
  { year: 2012, Barcelona: 10.5, Girona: 8.5, Lleida: 7.5, Tarragona: 9.5 },
  { year: 2013, Barcelona: 11, Girona: 9, Lleida: 8, Tarragona: 10 },
  { year: 2014, Barcelona: 10.8, Girona: 8.8, Lleida: 7.8, Tarragona: 9.8 },
  { year: 2015, Barcelona: 10.5, Girona: 8.5, Lleida: 7.5, Tarragona: 9.5 },
  { year: 2016, Barcelona: 10.2, Girona: 8.2, Lleida: 7.2, Tarragona: 9.2 },
  { year: 2017, Barcelona: 10, Girona: 8, Lleida: 7, Tarragona: 9 },
  { year: 2018, Barcelona: 9.8, Girona: 7.8, Lleida: 6.8, Tarragona: 8.8 },
  { year: 2019, Barcelona: 9.5, Girona: 7.5, Lleida: 6.5, Tarragona: 8.5 },
  { year: 2020, Barcelona: 10, Girona: 8, Lleida: 7, Tarragona: 9 },
  { year: 2021, Barcelona: 9.5, Girona: 7.5, Lleida: 6.5, Tarragona: 8.5 },
  { year: 2022, Barcelona: 9, Girona: 7, Lleida: 6, Tarragona: 8 },
  { year: 2023, Barcelona: 8, Girona: 6, Lleida: 5, Tarragona: 7 }
];

const blue = "#3b5fc0", yellow = "#ffd754", grey = "#c7c1bf", purple = "#a160af", orange = "#ff9c38", green = "#5ca34b", pink = "#f794b9", sky = "#61b0ff", red = "#ed393f", brown = "#a87a54";

const lineChartProvince = (width, height, province, color) => Plot.plot({
  width,
  height,
  marginRight: 60,
  marks: [
    Plot.lineY(dadesAtur, {x: "year", y:province, stroke: chroma(color).darken().hex(), strokeWidth: 3, title: province}),
    Plot.lineY(dadesAtur, {x: "year", y:province, stroke: chroma(color).darken().hex(), strokeWidth: 2, title: province, marker: "dot"}),
    Plot.lineY(dadesAtur, {x: "year", y:province, stroke: color, title: province, marker: "dot", curve: "monotone-x"}),
    Plot.text(dadesAtur, Plot.selectLast({x: "year", y: province, text: d => province, textAnchor: "start", dx: 6})),
  ],
  x: {
    label: "Any",
    tickFormat: d3.format("d")
  },
  y: {
    grid: true,
    domain: [5,11],
    label: "Taxa d'atur (%)"
  }
});

const MAPBOX_TOKEN = "pk.eyJ1IjoiZm5kdml0IiwiYSI6ImNseDR5dDV5dTBmeWMyaXNjemRkbDA3cHEifQ.HgSEJBTQzDFB-qBS2C4dvg";
```

# Exemples de codi

## Gràfics amb Plot
[*Plot*](https://observablehq.com/plot/what-is-plot) és la biblioteca de *JavaScript* que vam fer servir a l'assignatura de *Visualització de l'Informació* i que va ser especialment dissenyada per accelerar l'anàlisi exploratòria de dades.

Aquest exemple visualitza dades anuals d'atur per província a Catalunya.

```js echo
dadesAtur
```

${resize((width) => lineChart(width))}


```js echo
const lineChart = (width) => Plot.plot({
  width,
  height: width * 0.5,
  marginRight: 60,
  marks: [
    Plot.lineY(dadesAtur, {x: "year", y: "Barcelona", stroke: blue, title: "Barcelona", marker: true, curve: "monotone-x", tip: true}),
    Plot.lineY(dadesAtur, {x: "year", y: "Girona", stroke: yellow, title: "Girona", marker: true, curve: "monotone-x", tip: true}),
    Plot.lineY(dadesAtur, {x: "year", y: "Lleida", stroke: grey, title: "Lleida", marker: true, curve: "monotone-x", tip: true}),
    Plot.lineY(dadesAtur, {x: "year", y: "Tarragona", stroke: purple, title: "Tarragona", marker: true, curve: "monotone-x", tip: true}),
    Plot.text(dadesAtur, Plot.selectLast({x: "year", y: "Barcelona", text: d => "Barcelona", textAnchor: "start", dx: 6})),
    Plot.text(dadesAtur, Plot.selectLast({x: "year", y: "Girona", text: d =>  "Girona", textAnchor: "start", dx: 6})),
    Plot.text(dadesAtur, Plot.selectLast({x: "year", y: "Lleida", text: d =>  "Lleida", textAnchor: "start", dx: 6})),
    Plot.text(dadesAtur, Plot.selectLast({x: "year", y: "Tarragona", text: d =>  "Tarragona", textAnchor: "start", dx: 6}))
  ],
  x: {
    label: "Any",
    tickFormat: d3.format("d")
  },
  y: {
    grid: true,
    label: "Taxa d'atur (%)"
  }
});
```

Normalment, utilitzareu els **gràfics dins de targetes** en un panell de dades. Llegiu més sobre les [nostres guies sobre com estructurar panells per a aquest projecte](./guia) i sobre com funcionen les [*grids* a *Observable Framework*](https://observablehq.com/framework/markdown#grids).

A sota es mostra un exemple de quatre *cards* per a les quatre províncies.

```html echo
<div class="grid grid-cols-4" style="grid-auto-rows: 240px;">
  <div class="card">
    ${resize((width, height) => lineChartProvince(width, height, "Barcelona", blue))}
  </div>
  <div class="card">
    ${resize((width, height) => lineChartProvince(width, height, "Tarragona", purple))}
  </div>
  <div class="card">
    ${resize((width, height) => lineChartProvince(width, height, "Girona", yellow))}
  </div>
  <div class="card">
    ${resize((width, height) => lineChartProvince(width, height, "Lleida", grey))}
  </div>
</div>
```

## Mapes amb Mapbox
[*Mapbox*](https://www.mapbox.com/) és una eina i API per produïr mapes interactius en aplicacions web. En aquesta secció, explorarem com utilitzar *Mapbox* a *Observable Framework* per crear, per example, mapes coroplètics per mostrar dades geoespacials.

Aquest exemple mostra com crear un mapa coroplètic, que fa servir **color per representar la variable estadística al mapa**. En aquest cas es visualitzen unes dades inventades a quatre seccions censals a la provincia de Girona.

```js echo
const choropleth = display(document.createElement("div"));
choropleth.style = "height: 540px;";

const map = new mapboxgl.Map({
  container: choropleth,
  accessToken: MAPBOX_TOKEN,
  style: 'mapbox://styles/fndvit/clvnpq95k01jg01qz1px52jzf',
  center: [2.1745, 41.65],
  zoom: 6.8
});

const testData = [
  { mundissec: "17901101001", rate: 8 },
  { mundissec: "17022102003", rate: 6 },
  { mundissec: "17181201002", rate: 5 },
  { mundissec: "17044801002", rate: 7 }
  //S'entenc, oi?
];

const createColorExpression = (data) => {
  const colorExpression = [
    "step",
    ["get", "rate"],
    "#f0f0f0",
    5,
    "#fec3b8",
    6,
    "#c289a8",
    7,
    "#885198",
    8,
    "#4c1787"
  ];

  const matchExpression = ["match", ["get", "MUNDISSEC"]];

  data.forEach((entry) => {
    matchExpression.push(entry.mundissec, entry.rate);
  });

  matchExpression.push(0);

  colorExpression[1] = matchExpression;

  return colorExpression;
};

map.on('load', function () {
  map.addSource("seccen", {
      type: "vector",
      url: "mapbox://fndvit.3n29djx2",
      promoteId: "MUNDISSEC"
  });

  map.addLayer({
    id: "seccen-fill",
    type: "fill",
    source: "seccen",
    "source-layer": "seccen-dgddop",
    paint: {
      'fill-color': createColorExpression(testData),
    }
  }, "admin-1-boundary-bg");
});

```

## Carregadors de dades
Els carregadors de dades (*data loaders*) permeten generar instantànies de dades pre-processades durant el procés de construcció del projecte. Poden ser escrits en qualsevol llenguatge de programació i són útils per accedir, transformar i preparar dades per a la seva visualització.

### Avantatges dels carregadors de dades
* **Poliglotisme:** Pots utilitzar qualsevol llenguatge de programació que prefereixis, com *Python*, *R*, *SQL*, *JavaScript*, entre altres. Això facilita que equips diversos treballin amb les eines amb les quals estan més còmodes.
* **Rendiment:** Els carregadors de dades poden processar grans quantitats de dades en temps de construcció, la qual cosa redueix el temps de càrrega del client. Això resulta en pàgines més ràpides.
* **Optimització:** Permeten filtrar, agregar i minimitzar les dades enviades al client, millorant la seguretat i privacitat de les dades mostrades.

### Exemple de codi per a un carregador de dades en *JavaScript*
Suposem que volem carregar dades dels embassaments a Catalunya des de [l'API del Portal de Transparència de Catalunya](https://analisi.transparenciacatalunya.cat/Medi-Ambient/Quantitat-d-aigua-als-embassaments-de-les-Conques-/gn9e-3qhr/about_data).

```js run=false
const response = await fetch("https://analisi.transparenciacatalunya.cat/resource/gn9e-3qhr.json?$limit=32877");
if (!response.ok) throw new Error(`fetch failed: ${response.status}`);
const json = await response.json();

const data = json.map((d) => {
  const capacity = (100 * d.volum_embassat) / d.percentatge_volum_embassat;
  const date = new Date(d.dia);
  const pct = +d.percentatge_volum_embassat;
  const level = +d.volum_embassat;
  return { date, pct, level, capacity };
}).sort( (a,b) => a.date - b.date);

process.stdout.write(JSON.stringify(data));
```

```js
const response = await fetch("https://analisi.transparenciacatalunya.cat/resource/gn9e-3qhr.json?$limit=32877");
if (!response.ok) throw new Error(`fetch failed: ${response.status}`);
const json = await response.json();

const embassaments = json.map((d) => {
  const capacity = (100 * d.volum_embassat) / d.percentatge_volum_embassat;
  const date = new Date(d.dia);
  const pct = +d.percentatge_volum_embassat;
  const level = +d.volum_embassat;
  return { date, pct, level, capacity };
}).sort( (a,b) => a.date - b.date);
```

Aquest carregador de dades obté dades des d'una API, les transforma al format adequat i genera un fitxer *JSON* amb les dades dels embassaments.

### Com utilitzar els carregadors de dades
Si el carregador aquest es diu per exemple `embassaments.json.js`, haurà generat un fitxer `embassaments.json`: ara pots accedir-hi des del client utilitzant `FileAttachment`.

```js run=false
const embassaments = FileAttachment("data/dades.json").json();
```

`FileAttachment` retorna una `Promise`, podeu utilitzar les dades en un bloc de codi diferent només cridant `embassaments`.

```js echo
embassaments
```

Per a més informació i exemples sobre com escriure carregadors de dades en diferents llenguatges, pots visitar [la documentació d'*Observable Framework*](https://observablehq.com/framework/loaders).