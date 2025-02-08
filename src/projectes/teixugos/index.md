---
title: Exemples de codi
toc: true
---


<style>
  .button-container {
    display: flex;
    justify-content: space-around;
    gap: 1rem;
    flex-wrap: wrap;
  }

  .button-container .card {
    padding: 1rem;
    background-color: #f4f4f4;
    border: 1px solid #ccc;
    border-radius: 5px;
    text-align: center;
    font-size: 1.2rem;
    cursor: pointer;
    transition: background-color 0.3s;
    flex: 1 1 150px;
    margin: 0.5rem;
  }

  .button-container .card .category {
    font-weight: 700;
    min-width: 50px;
  }

  .button-container .card:hover {
    background-color: #e0e0e0;
  }

  @media (max-width: 768px) {
    .button-container {
      justify-content: center;
    }
    .button-container .card {
      flex: 1 1 45%;
      font-size: 1rem;
    }
  }

  /* Estilo para el contenedor del gráfico */
  #charts-container {
    width: 100%;
    height: 600px; /* Ajustado para dar espacio al gráfico de barras */
    border: 1px solid #ccc;
    border-radius: 8px;
    margin-top: 1rem;
    background-color: #fafafa;
  }

  #violin-chart-container {
    width: 100%;
    height: 400px; /* Altura para el gráfico de violín */
    border: 1px solid #ccc;
    border-radius: 8px;
    margin-top: 1rem;
    background-color: #fafafa;
  }
</style>

<!-- Incluir la librería Plotly -->
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

<!-- Contenedor de los botones -->
<div class="button-container">
    <div class="card" id="energia_calefacci" onclick="changeValue('energia_calefacci')">
        🔥 Energia calefacció
    </div>
    <div class="card" id="energia_refrigeraci" onclick="changeValue('energia_refrigeraci')">
        ❄️ Energia refrigeració
    </div>
    <div class="card" id="energia_acs" onclick="changeValue('energia_acs')">
        💧 Energia ACS
    </div>
    <div class="card" id="energia_enllumenament" onclick="changeValue('energia_enllumenament')">
        💡 Energia enllumenament
    </div>
    <div class="card" id="consum_d_energia_final" onclick="changeValue('consum_d_energia_final')">
        ⚡ Consum d'energia final
    </div>
    <div class="card" id="xarxa_districte" onclick="changeValue('xarxa_districte')">
        🌐 Xarxa districte
    </div>
    <div class="card" id="energia_geotermica" onclick="changeValue('energia_geotermica')">
        🌍 Energia geotèrmica
    </div>
    <div class="card" id="sistema_biomassa" onclick="changeValue('sistema_biomassa')">
        🌱 Sistema biomassa
    </div>
</div>

<div id="charts-container">
  <!-- Gráfico de barras acumuladas se generará aquí -->
</div>

<div id="violin-chart-container">
  <!-- Gráfico de violín se generará aquí -->
</div>

<script type="module">
  const data = {
    "A": {
        "energia_calefacci": 26818.68,
        "energia_refrigeraci": 7153.94,
        "energia_acs": 11188.02,
        "energia_enllumenament": 10996.43,
        "consum_d_energia_final": 35796.41,
        "xarxa_districte": 16.0,
        "energia_geotermica": 12.0,
        "sistema_biomassa": 111.0
    },
    "B": {
        "energia_calefacci": 108020.92,
        "energia_refrigeraci": 23345.88,
        "energia_acs": 31646.01,
        "energia_enllumenament": 50521.63,
        "consum_d_energia_final": 112415.88,
        "xarxa_districte": 6.0,
        "energia_geotermica": 6.0,
        "sistema_biomassa": 48.0
    },
    "C": {
        "energia_calefacci": 593386.76,
        "energia_refrigeraci": 74713.25,
        "energia_acs": 129467.01,
        "energia_enllumenament": 202231.69,
        "consum_d_energia_final": 530756.58,
        "xarxa_districte": 15.0,
        "energia_geotermica": 10.0,
        "sistema_biomassa": 96.0
    },
    "D": {
        "energia_calefacci": 1182804.75,
        "energia_refrigeraci": 116231.07,
        "energia_acs": 415386.73,
        "energia_enllumenament": 202074.24,
        "consum_d_energia_final": 1021674.87,
        "xarxa_districte": 26.0,
        "energia_geotermica": 11.0,
        "sistema_biomassa": 170.0
    },
    "E": {
        "energia_calefacci": 8260432.68,
        "energia_refrigeraci": 470617.36,
        "energia_acs": 3511404.58,
        "energia_enllumenament": 221679.19,
        "consum_d_energia_final": 7959047.88,
        "xarxa_districte": 143.0,
        "energia_geotermica": 36.0,
        "sistema_biomassa": 503.0
    },
    "F": {
        "energia_calefacci": 2402098.48,
        "energia_refrigeraci": 126704.29,
        "energia_acs": 1024098.37,
        "energia_enllumenament": 156828.08,
        "consum_d_energia_final": 2449881.99,
        "xarxa_districte": 29.0,
        "energia_geotermica": 9.0,
        "sistema_biomassa": 104.0
    },
    "G": {
        "energia_calefacci": 4462466.41,
        "energia_refrigeraci": 206727.06,
        "energia_acs": 1945024.48,
        "energia_enllumenament": 233509.68,
        "consum_d_energia_final": 4482966.76,
        "xarxa_districte": 32.0,
        "energia_geotermica": 18.0,
        "sistema_biomassa": 99.0
    }
  };

  const ratings = {
    'sistema_biomassa': {
      'D': 4718,
      'C': 6700,
      'B': 5385,
      'A': 4767,
      'E': 983,
      'G': 273,
      'F': 422
    },
    'xarxa_districte': {
      'D': 517,
      'C': 739,
      'B': 535,
      'A': 579,
      'E': 154,
      'G': 112,
      'F': 108
    },
    'energia_geotermica': {
      'D': 154,
      'C': 275,
      'B': 188,
      'A': 269,
      'E': 54,
      'G': 27,
      'F': 21
    },
    'rehabilitacio_energetica': {
      'D': 2381,
      'C': 3868,
      'B': 4164,
      'A': 5791,
      'E': 509,
      'G': 268,
      'F': 286
    }
  };

// Llamar a la función para actualizar las cards al cargar la página
window.onload = updateCategoryValues;

  const energyColors = {
    "energia_calefacci": "#FF5733", 
    "energia_refrigeraci": "#33C1FF", 
    "energia_acs": "#FFDD33", 
    "energia_enllumenament": "#FFC300", 
    "consum_d_energia_final": "#7DFF33", 
    "xarxa_districte": "#8E44AD", 
    "energia_geotermica": "#1ABC9C", 
    "sistema_biomassa": "#F39C12" 
  };

  const categories = Object.keys(data);  
  const energies = Object.keys(data["A"]);

  const plotData = energies.map(energy => {
    return {
      x: categories,
      y: categories.map(category => data[category][energy]),
      name: formatLabel(energy),
      type: 'bar',
      stackgroup: 'one',
      marker: { color: energyColors[energy] }
    };
  });

  const layoutBars = {
    barmode: 'stack',
    title: 'Distribución de Energías por Categoría',
    xaxis: { title: 'Categorías Energéticas' },
    yaxis: { title: 'Valor Energético' },
    margin: { t: 40, r: 40, b: 60, l: 60 },
    plot_bgcolor: '#f7f7f7',
    paper_bgcolor: '#fafafa'
  };

  const plotViolinData = Object.keys(ratings).map(energy => {
    return {
      x: new Array(Object.keys(ratings[energy]).length).fill(formatLabel(energy)),
      y: Object.values(ratings[energy]),
      type: 'violin',
      box: { visible: true },
      line: { color: 'black' },
      meanline: { visible: true },
      name: formatLabel(energy),
      fillcolor: energyColors[energy],  
      opacity: 0.6
    };
  });

  const layoutViolin = {
    title: 'Distribución de Calificaciones por Energía',
    yaxis: { title: 'Calificación' },
    margin: { t: 40, r: 40, b: 60, l: 60 },
    plot_bgcolor: '#f7f7f7',
    paper_bgcolor: '#fafafa'
  };

  function formatLabel(label) {
    return label.replace(/_/g, ' ').replace(/\b\w/g, char => char.toUpperCase());  
  }

  function changeValue(value) {
    Plotly.newPlot('charts-container', plotData, layoutBars);
    Plotly.newPlot('violin-chart-container', plotViolinData, layoutViolin);
  }

  Plotly.newPlot('charts-container', plotData, layoutBars);
  Plotly.newPlot('violin-chart-container', plotViolinData, layoutViolin);

  const means = {
    "energia_calefacci": 142.469348,
    "energia_refrigeraci": 8.763096,
    "energia_acs": 52.894144,
    "energia_enllumenament": 5.701210,
    "consum_d_energia_final": 132.746740,
    "xarxa_districte": 0.003197,
    "energia_geotermica": 0.001269,
    "sistema_biomassa": 0.025199
  };

  function updateCategoryValues() {
    Object.keys(energyColors).forEach(energy => {
      const categoryCard = document.getElementById(energy);
      // Asignar el texto con el valor medio y mediano
      categoryCard.innerHTML += `
        <br> <strong> Media: ${means[energy].toFixed(2)} </strong>
      `;
    });
  }

  // Llamar a la función para actualizar las cards al cargar la página
  window.onload = updateCategoryValues;
</script>

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

const municipiosData = [
  { codi_municipi: 171788, nombre: "Sant Pere Pescador", latitud: 42.17716, longitud: 3.0968, valor_lectura: 27000.0, previsio: 431.0 },
  { codi_municipi: 171789, nombre: "Figueres", latitud: 42.2654, longitud: 2.9558, valor_lectura: 35000.0, previsio: 300.0 },
  { codi_municipi: 171790, nombre: "Empuriabrava", latitud: 42.2584, longitud: 3.1122, valor_lectura: 50000.0, previsio: 500.0 },
  { codi_municipi: 171791, nombre: "Castelló d'Empúries", latitud: 42.2680, longitud: 2.9587, valor_lectura: 40000.0, previsio: 600.0 },
  { codi_municipi: 171792, nombre: "Roses", latitud: 42.2710, longitud: 3.1757, valor_lectura: 60000.0, previsio: 800.0 },
  { codi_municipi: 171793, nombre: "Vilajuïga", latitud: 42.3165, longitud: 3.0711, valor_lectura: 32000.0, previsio: 350.0 },
  { codi_municipi: 171794, nombre: "La Jonquera", latitud: 42.3971, longitud: 2.9074, valor_lectura: 15000.0, previsio: 250.0 },
  { codi_municipi: 171795, nombre: "L'Escala", latitud: 42.1207, longitud: 3.1404, valor_lectura: 45000.0, previsio: 500.0 },
  { codi_municipi: 171796, nombre: "Palau-saverdera", latitud: 42.3003, longitud: 3.0701, valor_lectura: 37000.0, previsio: 550.0 },
  { codi_municipi: 171797, nombre: "El Port de la Selva", latitud: 42.3051, longitud: 3.3149, valor_lectura: 48000.0, previsio: 650.0 },
  { codi_municipi: 170724, nombre: "Girona", latitud: 41.9794, longitud: 2.8214, valor_lectura: 80000.0, previsio: 1200.0 },
  { codi_municipi: 170725, nombre: "Salt", latitud: 41.9791, longitud: 2.8320, valor_lectura: 20000.0, previsio: 300.0 },
  { codi_municipi: 170726, nombre: "Banyoles", latitud: 42.1169, longitud: 2.7565, valor_lectura: 35000.0, previsio: 400.0 },
  { codi_municipi: 170727, nombre: "Figueres", latitud: 42.2654, longitud: 2.9558, valor_lectura: 47000.0, previsio: 500.0 },
  { codi_municipi: 170728, nombre: "Olot", latitud: 42.1807, longitud: 2.4894, valor_lectura: 30000.0, previsio: 600.0 },
  { codi_municipi: 170729, nombre: "Cervià de les Garrigues", latitud: 41.4842, longitud: 0.6999, valor_lectura: 25000.0, previsio: 400.0 },
  { codi_municipi: 170730, nombre: "La Bisbal d'Empordà", latitud: 41.9734, longitud: 3.0122, valor_lectura: 38000.0, previsio: 450.0 },
  { codi_municipi: 170731, nombre: "Calonge", latitud: 41.8594, longitud: 3.0211, valor_lectura: 42000.0, previsio: 500.0 },
  { codi_municipi: 170732, nombre: "Palamós", latitud: 41.8506, longitud: 3.1305, valor_lectura: 60000.0, previsio: 750.0 },
  { codi_municipi: 170733, nombre: "Castell-Platja d'Aro", latitud: 41.8189, longitud: 3.0389, valor_lectura: 55000.0, previsio: 650.0 },
  { codi_municipi: 170734, nombre: "Begur", latitud: 41.9760, longitud: 3.2150, valor_lectura: 40000.0, previsio: 500.0 },
  { codi_municipi: 170735, nombre: "Pals", latitud: 41.9793, longitud: 3.1997, valor_lectura: 45000.0, previsio: 600.0 },
  { codi_municipi: 170736, nombre: "Palafrugell", latitud: 41.9062, longitud: 3.2202, valor_lectura: 53000.0, previsio: 700.0 },
  { codi_municipi: 170737, nombre: "La Bisbal d'Empordà", latitud: 41.9734, longitud: 3.0122, valor_lectura: 37000.0, previsio: 450.0 },
  { codi_municipi: 170738, nombre: "La Cellera de Ter", latitud: 41.9373, longitud: 2.4843, valor_lectura: 22000.0, previsio: 300.0 },
  { codi_municipi: 170739, nombre: "Sils", latitud: 41.8481, longitud: 2.8192, valor_lectura: 39000.0, previsio: 500.0 },
  { codi_municipi: 170740, nombre: "Riudellots de la Selva", latitud: 41.8411, longitud: 2.7632, valor_lectura: 35000.0, previsio: 450.0 },
  { nombre: "Tarragona", latitud: 41.1182, longitud: 1.2445, valor_lectura: 20000, previsio: 500 },
  { nombre: "Reus", latitud: 41.1481, longitud: 1.1055, valor_lectura: 15000, previsio: 300 },
  { nombre: "Salou", latitud: 41.0750, longitud: 1.1588, valor_lectura: 12000, previsio: 400 },
  { nombre: "Cambrils", latitud: 41.0746, longitud: 1.2505, valor_lectura: 10000, previsio: 350 },
  { nombre: "Vila-seca", latitud: 41.1217, longitud: 1.1503, valor_lectura: 8000, previsio: 450 },
  { nombre: "La Pineda", latitud: 41.1065, longitud: 1.1719, valor_lectura: 7000, previsio: 200 },
  { nombre: "Amposta", latitud: 40.7733, longitud: 0.6858, valor_lectura: 6000, previsio: 250 },
  { nombre: "Alcanar", latitud: 40.5350, longitud: 0.5295, valor_lectura: 4000, previsio: 300 },
  { nombre: "Tarragonès", latitud: 41.1375, longitud: 1.2400, valor_lectura: 15000, previsio: 500 },
  { nombre: "Cunit", latitud: 41.1841, longitud: 1.6502, valor_lectura: 9000, previsio: 350 },
  { nombre: "Segur de Calafell", latitud: 41.1092, longitud: 1.5741, valor_lectura: 11000, previsio: 400 },
  { nombre: "Calafell", latitud: 41.2060, longitud: 1.5731, valor_lectura: 9500, previsio: 380 },
  { nombre: "Vendrell", latitud: 41.2119, longitud: 1.6117, valor_lectura: 13000, previsio: 450 },
  { nombre: "El Vendrell", latitud: 41.2163, longitud: 1.5371, valor_lectura: 14000, previsio: 600 },
  { nombre: "Deltebre", latitud: 40.7193, longitud: 0.7033, valor_lectura: 8000, previsio: 320 },
  { nombre: "Camarles", latitud: 40.8016, longitud: 0.6622, valor_lectura: 4500, previsio: 270 },
  { nombre: "La Canonja", latitud: 41.1322, longitud: 1.2044, valor_lectura: 7500, previsio: 320 },
  { nombre: "Ametlla de Mar", latitud: 40.9308, longitud: 0.6222, valor_lectura: 8500, previsio: 300 },
  { nombre: "Montblanc", latitud: 41.3000, longitud: 1.1000, valor_lectura: 7000, previsio: 290 },
  { nombre: "Falset", latitud: 41.2325, longitud: 0.8411, valor_lectura: 6000, previsio: 280 },
  { nombre: "Móra d'Ebre", latitud: 41.1554, longitud: 0.7417, valor_lectura: 5000, previsio: 250 },
  { nombre: "Benifallet", latitud: 40.9536, longitud: 0.4811, valor_lectura: 3000, previsio: 220 },
  { nombre: "Vila-Seca", latitud: 41.1406, longitud: 1.1569, valor_lectura: 9500, previsio: 430 }

  // Puedes seguir añadiendo más municipios siguiendo este formato
];

const geojson = {
  type: "FeatureCollection",
  features: municipiosData.map(municipio => {
    return {
      type: "Feature",
      geometry: {
        type: "Point",
        coordinates: [municipio.longitud, municipio.latitud]
      },
      properties: {
        nombre: municipio.nombre,
        valor_lectura: municipio.valor_lectura,
        previsio: municipio.previsio
      }
    };
  })
};

map.on('load', function () {
  map.addSource('municipios', {
    type: 'geojson',
    data: geojson
  });

  map.addLayer({
    id: 'municipios-bubbles',
    type: 'circle',
    source: 'municipios',
    paint: {
      // Determinar el radio en función de valor_lectura (círculos más grandes)
      'circle-radius': [
        'interpolate', ['linear'], ['get', 'valor_lectura'],
        0, 10, // Radio mínimo en píxeles
        1000000, 100 // Radio máximo en píxeles (ajústalo según tus datos)
      ],
      // Determinar el color del círculo según Previsió/Crèdits inicials consolidats
      'circle-color': [
        'interpolate', ['linear'], ['get', 'previsio'],
        0, '#e0f7e0', // Verde muy claro para valores bajos
        500, '#66bb6a', // Verde medio
        1000, '#006400' // Verde oscuro para valores altos
      ],
      'circle-opacity': 0.7
    }
  });
});

// Usar FileAttachment para cargar el archivo CSV
const estaciones = FileAttachment("dades_estacions.csv").csv();
estaciones.then(data => {
  console.log(data); // Verifica que los datos están llegando correctamente

  // Crear un array de características GeoJSON para las estaciones
  const geojson = {
    type: "FeatureCollection",
    features: data.map(station => ({
      type: "Feature",
      geometry: {
        type: "Point",
        coordinates: [parseFloat(station.longitud), parseFloat(station.latitud)] // Longitud, Latitud
      },
      properties: {
        nombre: station.nom_estacio
      }
    }))
  };

  // Añadir el GeoJSON como una fuente en el mapa
  map.on('load', function () {
    map.addSource('estaciones', {
      type: 'geojson',
      data: geojson
    });

    // Añadir una capa para los puntos (círculos)
    map.addLayer({
      id: 'estaciones-circles',
      type: 'circle',
      source: 'estaciones',
      paint: {
        'circle-radius': 5, // Tamaño del punto
        'circle-color': '#1E90FF', // Color azul
        'circle-opacity': 0.8 // Opacidad
      }
    });
  });
});

const testData = [
  { mundissec: "17901101001", rate: 8 },
  { mundissec: "17022102003", rate: 6 },
  { mundissec: "17181201002", rate: 5 },
  { mundissec: "17044801002", rate: 7 }
];

// Datos de los parques naturales con latitud y longitud
const parques = [
  { nombre: "Parque Nacional d'Aigüestortes i Estany de Sant Maurici", lat: 42.5833, lon: 0.9833 },
  { nombre: "Parque Natural dels Aiguamolls de l'Empordà", lat: 42.2567, lon: 3.0800 },
  { nombre: "Parque Natural de l'Alt Pirineu", lat: 42.6167, lon: 1.2667 },
  { nombre: "Parque Natural del Cadí-Moixeró", lat: 42.3167, lon: 1.7500 },
  { nombre: "Parque Natural del Cap de Creus", lat: 42.3167, lon: 3.2833 },
  { nombre: "Parque Natural de Capçaleres del Ter i del Freser", lat: 42.3925, lon: 2.1586 },
  { nombre: "Parque Natural del Delta de l'Ebre", lat: 40.7094, lon: 0.7350 },
  { nombre: "Parque Natural del Massís del Montseny", lat: 41.7667, lon: 2.4167 },
  { nombre: "Parque Natural del Montgrí, les Illes Medes i Baix Ter", lat: 42.0450, lon: 3.2044 },
  { nombre: "Parque Natural de la Muntanya de Montserrat", lat: 41.5958, lon: 1.8342 },
  { nombre: "Parque Natural dels Ports", lat: 40.8167, lon: 0.3333 },
  { nombre: "Parque Natural de Sant Llorenç del Munt i l'Obac", lat: 41.6614, lon: 2.0069 },
  { nombre: "Parque Natural de la Serra del Montsant", lat: 41.2667, lon: 0.8500 },
  { nombre: "Parque Natural de la Serra de Collserola", lat: 41.4333, lon: 2.1000 },
  { nombre: "Parque Natural de la Zona Volcànica de la Garrotxa", lat: 42.1500, lon: 2.5000 },
  { nombre: "Paraje natural d'interès nacional del Massís de l'Albera", lat: 42.4286, lon: 2.8783 },
  { nombre: "Paraje natural d'interès nacional de la Vall del Monestir de Poblet", lat: 41.3608, lon: 1.0525 }
];

// Función para agregar los puntos verdes en las coordenadas
map.on('load', function () {
  // Agregar capa choropleth
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

  // Agregar los puntos verdes para cada parque natural
  parques.forEach(parque => {
    const marker = new mapboxgl.Marker({
      color: 'green' // Punto verde
    })
    .setLngLat([parque.lon, parque.lat])
    .addTo(map);

    // Agregar un popup con el nombre del parque cuando el marcador es hover
    const popup = new mapboxgl.Popup({ offset: 25 })
      .setHTML(parque.nombre);

    marker.setPopup(popup); // Asocia el popup al marcador
  });
});

// Crear la expresión de colores para la capa choropleth
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

```


