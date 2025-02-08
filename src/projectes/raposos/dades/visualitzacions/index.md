---
title: Raposos
toc: true
---

# Visualitzacions

### El seu exemple:

```js
const MAPBOX_TOKEN = "pk.eyJ1IjoiZm5kdml0IiwiYSI6ImNseDR5dDV5dTBmeWMyaXNjemRkbDA3cHEifQ.HgSEJBTQzDFB-qBS2C4dvg";
```

```js
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

### Certificats groupped by mundissec

```js
const certificats_groupby_mundissec = FileAttachment("../emissions-per-seccion_xaquin.json").json();
```

```js
certificats_groupby_mundissec
```


```js 
const choropleth_0 = display(document.createElement("div"));
choropleth.style = "height: 540px;";

const map = new mapboxgl.Map({
  container: choropleth,
  accessToken: MAPBOX_TOKEN,
  style: 'mapbox://styles/fndvit/clvnpq95k01jg01qz1px52jzf',
  center: [2.1745, 41.65],
  zoom: 6.8
});

// Funció per generar l'expressió de colors segons mean_emissions
const createColorExpression = (data) => {
  const emissions = data.map(entry => entry.mean_emissions);
  const minEmissions = Math.min(...emissions);
  const maxEmissions = Math.max(...emissions);
  const medianEmissions = emissions.sort((a, b) => a - b)[Math.floor(emissions.length / 2)];

  const colorExpression = [
    "step",
    ["get", "rate"],
    "#f0f0f0",  // Emissions molt baixes (0)
    10, "#a1d99b",  // Verd clar per a emissions de 10
    20, "#74c476",  // Verd mitjà per a emissions de 20
    30, "#31a354",  // Verd fosc per a emissions de 30
    40, "#fe9929",  // Vermell clar per a emissions de 40
    50, "#d95f0e",  // Vermell mitjà per a emissions de 50
    60, "#99000d",  // Vermell fosc per a emissions de 60
    70, "#d73027"   // Vermell fosc per a emissions de 70
  ];

  const matchExpression = ["match", ["get", "MUNDISSEC"]];
  data.forEach((entry) => {
    matchExpression.push(entry.mundissec, entry.mean_emissions);
  });
  matchExpression.push(0);
  colorExpression[1] = matchExpression;

  return { colorExpression, minEmissions, medianEmissions, maxEmissions };
};

map.on('load', function () {
  // Retornar els valors de les emissions, incloent el mínim, mitjà i màxim
  const { colorExpression, minEmissions, medianEmissions, maxEmissions } = createColorExpression(certificats_groupby_mundissec);

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
      'fill-color': colorExpression,
      'fill-opacity': 0.75
    }
  }, "admin-1-boundary-bg");

  // Crear la llegenda amb barra de colors
  const legend = document.createElement('div');
  legend.className = 'mapboxgl-ctrl mapboxgl-ctrl-group mapboxgl-ctrl'; // Usar la classe del control per a l'estil

  const legendTitle = document.createElement('div');
  legendTitle.className = 'legend-title';
  legendTitle.textContent = 'Mean Emissions';
  legend.appendChild(legendTitle);

  // Crear la barra de colors amb més punts de transició
  const colorBar = document.createElement('div');
  colorBar.className = 'color-bar';
  colorBar.style.height = '15px';  // Ajustar la altura
  colorBar.style.width = '150px';  // Ajustar el ancho
  colorBar.style.background = 'linear-gradient(to right, #f0f0f0, #a1d99b, #74c476, #31a354, #fe9929, #d95f0e, #99000d, #d73027)';
  legend.appendChild(colorBar);

  // Crear els valors de la llegenda
  const legendValues = document.createElement('div');
  legendValues.className = 'legend-values';
  legendValues.style.display = 'flex';
  legendValues.style.justifyContent = 'space-between';
  legendValues.style.fontSize = '12px';

  // Mostrar els valors mínim, mitjà i màxim
  const minValue = document.createElement('div');
  minValue.className = 'legend-value';
  minValue.textContent = minEmissions.toFixed(2);
  legendValues.appendChild(minValue);

  const medianValue = document.createElement('div');
  medianValue.className = 'legend-value';
  medianValue.textContent = medianEmissions.toFixed(2);
  legendValues.appendChild(medianValue);

  const maxValue = document.createElement('div');
  maxValue.className = 'legend-value';
  maxValue.textContent = maxEmissions.toFixed(2);
  legendValues.appendChild(maxValue);

  legend.appendChild(legendValues);

  // Afegir la llegenda al mapa a la part superior esquerra
  map.getContainer().appendChild(legend);

  // Estils CSS per a posicionar la llegenda
  legend.style.position = 'absolute';
  legend.style.top = '10px';
  legend.style.left = '10px';
  legend.style.backgroundColor = 'rgba(255, 255, 255, 0.7)';
  legend.style.padding = '10px';
  legend.style.borderRadius = '8px';
});
```


<div class="grid grid-cols-4">
  <div class="card example wrong grid-colspan-3">
    ${choropleth_0}
  </div>
</div>

