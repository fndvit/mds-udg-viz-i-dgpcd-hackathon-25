---
title: Raposos
toc: true
---

# Hola

```js
dades_ine = FileAttachment("./dades/dataset_ine.md").json();
```

```js
dades_municipis = FileAttachment("./dades/divisions-administratives-municipis.json").json();
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