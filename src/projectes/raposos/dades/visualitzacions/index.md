---
title: Raposos
toc: true
---

# Visualitzacions


```js
const rendaPerMunicipi = new Map(dades_ine.map(d => [d.poblacio, +d.renta_neta_mitja_por_persona]));
```

```js
const valorsRenda = Array.from(rendaPerMunicipi.values()).filter(d => d > 0); // Excloem els 0
```

```js
const dominiRenda = [Math.min(...valorsRenda), Math.max(...valorsRenda)];
```

```js
Plot.plot({
  width: 400,
  height: 400,
  color: {
    type: "linear", // Canviem de "quantile" a "linear"
    scheme: "Reds",
    label: "Renda Neta Mitjana per Persona (€)",
    domain: dominiRenda, // Especifiquem el domini
    legend: true
  },
  marks: [
    Plot.geo(dades_municipis, {
      fill: d => rendaPerMunicipi.get(d.properties.NOMMUNI) || dominiRenda[0], // Assignem el mínim si no hi ha dades
      title: d => `${d.properties.NOMMUNI}: ${rendaPerMunicipi.get(d.properties.NOMMUNI) || "Sense dades"} €`,
      tip: true
    })
  ]
})
```



```js
const dades_ine = FileAttachment("../dataset_ine.csv").csv();
```

```js
const dades_municipis = FileAttachment("../divisions-administratives-municipis.json").json();
```

```js
Plot.plot({
  width: 400,
  height: 400,
  color: {
    type: "quantile",
    scheme: "Reds",
    label: "Àrea Municipis Catalunya (km²)",
    legend: true
  },
  marks: [
    Plot.geo(dades_municipis, {
      fill: (d) => d.properties.AREAM5000,
      title: (d) => `${d.properties.NOMMUNI} (${(d.properties.AREAM5000).toFixed(2)} km²)`,
      tip: true
    })
  ]
})
```
