---
title: Raposos
toc: true
---

# Visualitzacions

```js
const MAPBOX_TOKEN = "pk.eyJ1IjoiZm5kdml0IiwiYSI6ImNseDR5dDV5dTBmeWMyaXNjemRkbDA3cHEifQ.HgSEJBTQzDFB-qBS2C4dvg";
```

```js
const mapa_socioeconomic = FileAttachment("../../../../dades/raposos/mapa_socioeconomic.csv").csv();
```

```js
mapa_socioeconomic
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
  ${resize((width) => choropleth)}
  </div>
  <div class="card">

  </div>
  <div class="card">

  </div>
</div>

<div class="grid grid-cols-3">
  <div class="card grid-colspan-3">

  </div>  
</div>

<div class="card">
  <h1>Interpretació del camp Ratio</h1>

  Aproximació en forma de valor entre 0 i 1 de la millora en l'estalvi per € invertit en actuacions de millora d'edificacions. La taula es mostra unificada per districte censal.
</div>


```js
const codi_postal = view(
  Inputs.text({
    label: "Codi Postal",
    placeholder: "00000",
    type: "number",
    maxlength: 5
  })
);
```

```js
view(Inputs.table(
  mapa_socioeconomic
  .filter((e)=> e.codi_postal.startsWith(codi_postal))
  .sort((a,b) => {
    return b.ratio_norm - a.ratio_norm;
  }).map((e) => {
    return {
      "Codi Districte": e.codi_districte,
      "Codi Postal": e.codi_postal,
      "Poblacio": e.poblacio,
      "Renta Mitja per persona": (+e.renta_neta_mitja_por_persona).toFixed(2),
      "Gini": (+e.indice_gini).toFixed(2),
      "Ratio": (+e.ratio_norm).toFixed(4),
    };
  }),
  {
    width: {
      "Codi Districte": 120,
      "Codi Postal": 100,
      "Poblacio": 150,
      "Gini": 100,
      "Ratio": 100,
    },
    align: {
      "Codi Districte": "center",
      "Codi Postal": "center",
      "Poblacio": "center",
      "Renta Mitja per persona": "center",
      "Gini": "center",
      "Ratio": "center",
    },
  }
));
```