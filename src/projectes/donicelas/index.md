---
title: Intro projectes
toc: false
---

<style>
  img {
    border-radius: 1rem;
    box-shadow: 0 0 1rem rgba(0,0,0,0.15);
    max-width: 42rem;
    margin: 1rem;
  }
</style>

# Relation with GDP and Energy Efficiency

The main goal of this project is to analyze the relationship between energy efficiency and GDP in Catalonia.  
We will use the data from the energy efficiency certificates and the GDP of Catalonia to analyze the relationship between these two variables.

```js
// Importar librerías necesarias.
import * as d3 from "d3";
import * as Plot from "@observablehq/plot";

// 1. Cargar el CSV. Asegúrate de que el archivo adjunto se llame EXACTAMENTE "taula1.csv"
//    (sin la ruta "./dades/" a menos que así se muestre en la lista de archivos adjuntos).
const csvData = await FileAttachment("./dades/taula1.csv").csv({ typed: true });

// 2. Parsear las fechas (formato: YYYY-MM-DD).
const parseDate = d3.timeFormat("%Y-%m-%d");
const parsedData = csvData.map(d => ({
  Fecha: parseDate(d.Fecha),
  Categoria: d.Categoria,
  Valor: +d.Valor // Asegurarse de que sea número
}));

// 3. Crear un formateador para el eje X.
const formatDate = d3.timeFormat("%Y-%m");
```
# Visualitzation of the data
```js echo
parsedData
```

```js

// 4. Función que genera el gráfico.
const lineChart = (width) => Plot.plot({
  width,
  height: width * 0.5,
  marginRight: 60,
  marks: [
    // Línea con marcadores y tooltips.
    Plot.lineY(parsedData, {
      x: "Fecha",
      y: "Valor",
      stroke: "Categoria",
      marker: true,
      curve: "monotone-x",
      tip: true
    }),
    // Etiquetas de texto para el último punto de cada categoría.
    Plot.text(parsedData, Plot.selectLast({
      x: "Fecha",
      y: "Valor",
      z: "Categoria",
      text: "Categoria",
      textAnchor: "start",
      dx: 6,
    }))
  ],
  x: {
    label: "Fecha",
    tickFormat: formatDate, // Usamos la función de formateo.
  },
  y: {
    grid: true,
    label: "Valor",
  },
  color: {
    // Puedes activar un esquema de colores comentando la siguiente línea:
    // scheme: "category10"
  }
});

// 5. Devolver el gráfico para que se muestre en la celda.
lineChart(600);
```
${resize((width) => lineChart(width))}