---
title: Raposos
toc: true
---

# Visualitzacions

```js
const MAPBOX_TOKEN = "pk.eyJ1IjoiZm5kdml0IiwiYSI6ImNseDR5dDV5dTBmeWMyaXNjemRkbDA3cHEifQ.HgSEJBTQzDFB-qBS2C4dvg";

const createColorExpression = (data, id, join, scheme) => {
  const { id: idJoin, prop: propJoin } = join;
  const { domain, range } = scheme;

  const colors = range.flatMap((color, index) => {
    return index < domain.length ? [color, domain[index]] : [color];
  });

  const colorExpression = ["step", ["get", propJoin], ...colors];

  const matchExpression = ["match", ["get", id]];

  data.forEach((entry) => {
    matchExpression.push(entry[idJoin], parseFloat(entry[propJoin])
    );
  });

  matchExpression.push(0);

  colorExpression[1] = matchExpression;

  return colorExpression;
}
```

```js
const mapa_socioeconomic = FileAttachment("../../../../dades/raposos/mapa_socioeconomic_cleaned.csv").csv();
```

```js
mapa_socioeconomic
```

```js 
const choropleth_0 = display(document.createElement("div"));
choropleth_0.style = "height: 540px;";

const map = new mapboxgl.Map({
  container: choropleth_0,
  accessToken: MAPBOX_TOKEN,
  style: 'mapbox://styles/fndvit/clvnpq95k01jg01qz1px52jzf',
  center: [2.1745, 41.65],
  zoom: 6.8
});

console.log(createColorExpression(mapa_socioeconomic, "MUNDISSEC", {id: "mundissec_original", prop: "indice_gini"},
        {
          domain: [20,25,30,35,40,45,50],
          range: ['#ffffe0', '#c0eade', '#9dced6', '#80b1cc', '#6694c1', '#4e78b5', '#325da9', '#00429d']
        }
      ))

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
      'fill-color': createColorExpression(mapa_socioeconomic, "MUNDISSEC", {id: "mundissec_original", prop: "indice_gini"},
        {
          domain: [20,25,30,35,40,45,50],
          range: ['#ffffe0', '#c0eade', '#9dced6', '#80b1cc', '#6694c1', '#4e78b5', '#325da9', '#00429d']
        }
      )
    }
  }, "tunnel-simple");
});
```


```js 
const choropleth_1 = display(document.createElement("div"));
choropleth_1.style = "height: 540px;";

const map = new mapboxgl.Map({
  container: choropleth_1,
  accessToken: MAPBOX_TOKEN,
  style: 'mapbox://styles/fndvit/clvnpq95k01jg01qz1px52jzf',
  center: [2.1745, 41.65],
  zoom: 6.8
});

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
      'fill-color': createColorExpression(mapa_socioeconomic, "MUNDISSEC", {id: "mundissec_original", prop: "renta_neta_mitja_por_persona"},
        {
          domain: [0,4500,9000,13500,18000,22500,27000,31500],
          range: ['#ffffe0', '#d8f2e1', '#c0eade', '#9dced6', '#80b1cc', '#6694c1', '#4e78b5', '#325da9', '#003385']
        }
      )
    }
  }, "admin-1-boundary-bg");
});
```


```js 
const choropleth_2 = display(document.createElement("div"));
choropleth_2.style = "height: 540px;";

const map = new mapboxgl.Map({
  container: choropleth_2,
  accessToken: MAPBOX_TOKEN,
  style: 'mapbox://styles/fndvit/clvnpq95k01jg01qz1px52jzf',
  center: [2.1745, 41.65],
  zoom: 6.8
});

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
      'fill-color': createColorExpression(mapa_socioeconomic, "MUNDISSEC", {id: "mundissec_original", prop: "qualificacio_consum_energia_no_renovables"},
        {
          domain: [1,2,3,4,5,6,7],
          range: ['#ffffe0', '#c0eade', '#9dced6', '#80b1cc', '#6694c1', '#4e78b5', '#325da9', '#00429d']
        }
      )
    }
  }, "admin-1-boundary-bg");
});
```

<div class="grid grid-cols-4">
  <div class="card">

  </div>
  <div class="card">

  </div>
  <div class="card">

  </div>
  <div class="card">

  </div>
</div>


<div class="grid grid-cols-3">
  <div class="card">
    <h1>Mapa de Gini</h1>
    <h2>Distribució de l'Índex de Gini per seccions censals</h2>  ${resize((width) => choropleth_0)}
  </div>
  <div class="card">
    <h1>Mapa de Renda</h1>
    <h2>Distribució de la Renda Neta Mitjana per seccions censals</h2>  ${resize((width) => choropleth_1)}
  </div>
  <div class="card">
    <h1>Mapa de Consum d'Energia</h1>
    <h2>Distribució de la qualificació d'Eficiència d'Energies No Renovables per seccions censals</h2>  ${resize((width) => choropleth_2)}
  </div>
</div>

<div class="grid grid-cols-3">
  <div class="card grid-colspan-3">

  </div>  
</div>