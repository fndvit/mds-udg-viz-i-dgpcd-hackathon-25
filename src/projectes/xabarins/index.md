---
title: Xabaríns
toc: false
---

<style>
  img {
    border-radius: 1rem;
    box-shadow: 0 0 1rem rgba(0,0,0,0.15);
    max-width: 42rem;
    margin:1rem;
  }
</style>

# Xabaríns

## Relació entre Eficiència Energètica i Emissions de Carboni

Per analitzar la relació entre eficiència energètica i emissions de CO₂, primer hem comprovat la normalitat de la distribució.

A continuació, hem realitzat una ANOVA per comparar la variable numèrica "emissions_de_co2" amb tres variables categòriques:

- *Qualificació de Consum d’Energia Primària No Renovable*
- *Qualificació d’Emissions de CO₂*
- *Zona Climàtica*

Els resultats han estat els següents:

| Tipus de Qualificació | Estadístic F | p-Valor |
|-----------------------|-------------|---------|
| Qualificació de Consum d’Energia Primària No Renovable | 80688.64 | 0.00 |
| Qualificació d’Emissions de CO₂ | 112684.87 | 0.00 |
| Zona Climàtica | 2529.73 | 0.00 |

### Interpretació

Els valors de *p-valor* són tots significatius (0.00), cosa que indica diferències estadísticament rellevants entre els grups de cada variable categòrica en relació amb les emissions de CO₂. 

- La *qualificació d’emissions de CO₂* presenta l’F més alt, la qual cosa suggereix que aquesta variable té la relació més forta amb les emissions de CO₂.
- La *qualificació de consum d’energia primària no renovable* també mostra una relació molt significativa, confirmant que l’eficiència energètica té un impacte directe en les emissions.
- La *zona climàtica* té un efecte menor en comparació amb les altres dues variables, però continua sent estadísticament significativa.

Aquests resultats reforcen la idea que una millor eficiència energètica es tradueix en una reducció d’emissions de CO₂, mentre que la zona climàtica influeix però amb menys pes que les qualificacions energètiques.

## Resultats de Correlació

<table style="width: 400px; border-collapse: collapse;">
  <tr>
    <th style="width: 40%;">Tipus de Correlació</th>
    <th style="width: 30%;">Energia Primària</th>
    <th style="width: 30%;">Consum Final</th>
  </tr>
  <tr>
    <td>Pearson</td>
    <td>0.4412</td>
    <td>0.6251</td>
  </tr>
  <tr>
    <td>Spearman</td>
    <td>0.9555</td>
    <td>0.6085</td>
  </tr>
  <tr>
    <td>Kendall</td>
    <td>0.8401</td>
    <td>0.5113</td>
  </tr>
</table>


#### Correlació de Pearson  
Mesura la relació lineal entre variables. L'energia primària té una correlació moderada (0.4412) amb les emissions de CO2, mentre que el consum final presenta una correlació més forta (0.6251), indicant un impacte més directe sobre les emissions.

#### Correlació de Spearman  
Avalua relacions monòtones, independentment de si són lineals. L'energia primària té una correlació molt alta (0.9555) amb les emissions, suggerint que augmenta de manera constant amb aquestes. El consum final també mostra una relació positiva (0.6085), però menys intensa.

#### Correlació de Kendall  
Similar a Spearman, basada en dades ordenades. L'energia primària presenta una forta correlació (0.8401), confirmant una relació consistent amb les emissions. El consum final té una correlació més baixa (0.5113), suggerint que altres factors com l'eficiència energètica poden influir.

### Interpretació  
- L'energia primària té una correlació més forta amb les emissions que el consum final en tots els casos, indicant que el total d'energia utilitzada al sistema és un millor predictor d'emissions.  
- Les correlacions de Spearman i Kendall indiquen que l'energia primària afecta les emissions de manera més estable que el consum final, possiblement a causa de pèrdues en generació i transport.  
- El consum final també té una relació significativa amb les emissions, però pot estar afectat per l'eficiència energètica o l'ús de renovables.  

### Definicions  
*Energia primària no renovable:* energia en el seu estat original abans de ser transformada (petroli, gas natural, etc.). Inclou només fonts no renovables i pateix pèrdues en generació i transport.  

*Consum d’energia final:* energia que arriba als usuaris després de les pèrdues en generació i transport. Pot incloure fonts renovables i no renovables.


```js

import {FileAttachment} from "observablehq:stdlib";
const byQualification = FileAttachment("p1_groupby_qualification.csv").csv({typed: true});

```
```js
const type = view(Inputs.select(Object.keys(byQualification[0]).filter(d => d !== "qualificacio_demissions_de_co2"), {value: "steelblue", label: "Group by: "}));
```

```js
Plot.plot({
  marks: [
    Plot.barX(byQualification, { 
      y: "qualificacio_demissions_de_co2",  // Categoría en el eje Y
      x: type,                      // Valor numérico en el eje X
      fill: type                     // Color de las barras
    })
  ]
})

```

```js
const groupedData = FileAttachment("p2_groupedData.csv").csv({typed: true});
```
```js
const p1 = {
  marks: [
    Plot.barY(groupedData, { 
      x: "category", 
      y: "emissions_mean", 
      sort: { x: "y", reverse: true },
      fill: "red" 
    }),
    Plot.ruleY([0]) // Baseline at zero
  ],
  x: { label: "Qualification CO₂ Emissions" },
  y: { label: "Mean CO₂ Emissions" },
  marginLeft: 60,
  marginBottom: 50
};
```
```js
const groupedData2 = FileAttachment("p3_groupedData2.json").json();
```

```js
const p2 = {
  marginBottom:100,
  marks: [
    Plot.barY(
      groupedData2.flatMap(d => 
        (d.subcategories || []).map(sub => ({
          category: d.category,
          subcategory: sub.subcategory.length > 10 ? sub.subcategory.slice(0, 10) + "…" : sub.subcategory, // Truncate long names
          emissions_mean: sub.emissions_mean
        }))
      ), 
      { 
        x: "subcategory", 
        y: "emissions_mean", 
        fill: "category",  
        fx: "category",   
        tip: { format: { emissions_mean: ".2f" } } 
      }
    ),
    Plot.ruleY([0]) 
  ],
  x: { 
    label: "Building Type", 
    tickRotate: -45,
    tickSize: 4,
  },
  y: { label: "Mean CO₂ Emissions" },
  color: { legend: true, label: "Category" }, 
  marginLeft: 60,
  marginBottom: 80
};
```

<div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 100%;">
  <h2>Quins tipus d’edificis generen més emissions?</h2>
  <p>Comparant emissions segons la seva qualificació energ.</p>
  <div style="display: flex; width: 100%; align-items: center;">
    <div style="width: 53%; min-height: 400px;">${Plot.plot(p1)}</div>
    <div style="width: 47%; min-height: 450px;">${Plot.plot(p2)}</div>
  </div>
</div>

## Q5
```js
data = [
  { zona_climatica: "A", emissions_de_co2: 20, indice_energia: 50, us_edifici: "Residencial" },
  { zona_climatica: "A", emissions_de_co2: 40, indice_energia: 70, us_edifici: "Comercial" },
  { zona_climatica: "B", emissions_de_co2: 35, indice_energia: 65, us_edifici: "Industrial" },
  { zona_climatica: "B", emissions_de_co2: 25, indice_energia: 55, us_edifici: "Residencial" },
  { zona_climatica: "C", emissions_de_co2: 30, indice_energia: 60, us_edifici: "Comercial" },
  { zona_climatica: "C", emissions_de_co2: 45, indice_energia: 80, us_edifici: "Industrial" }
];

// Crear el scatter plot con facetas
Plot.plot({
  facet: {
    data: data,
    x: "zona_climatica"  // Se crean paneles por cada valor de zona_climatica
  },
  marks: [
    Plot.dot(data, {
      x: "emissions_de_co2",
      y: "indice_energia",
      fill: "us_edifici",  // El color depende de us_edifici
      r: 5 // Tamaño de los puntos
    }),
    Plot.frame() // Añadir bordes a los gráficos facetados
  ],
  color: {
    legend: true // Muestra la leyenda para el color
  }
})
```