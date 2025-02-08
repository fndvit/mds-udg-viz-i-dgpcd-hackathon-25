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
## Link Notebook
https://observablehq.com/@hackathon-xabarins/jacaton
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
const df_p1 = FileAttachment("df_p1.csv").csv({typed: true});
const tecnologies_ef = FileAttachment("tecnologies_ef.csv").csv({typed: true});
const bar_q5 = FileAttachment("bar_q5.csv").csv({typed: true});
```


```js
const groupedData = FileAttachment("p2_groupedData.csv").csv({typed: true});
```

```js
const groupBy = view(Inputs.select(Object.keys(df_p1[0]), {value: "steelblue", label: "Group by: "}));
```

```js
const secondGroupBy = view(Inputs.select(Object.keys(df_p1[0]), {value: "steelblue", label: "Group by: "}));
```

```js
const groupedData2 = Generators.observe(change => {
  change(
    Array.from(
      d3.rollup(
        groupedData,
        v => d3.mean(v, d => d.emissions_de_co2), // Ensure emissions_de_co2 exists
        d => d[groupBy],  // Ensure d[groupBy] is a valid key
        d => d[secondGroupBy] // Ensure d[secondGroupBy] is a valid key
      ),
      ([key1, subMap]) => ({
        category: key1 ?? "Undefined",
        subcategories: Array.from(subMap, ([key2, value]) => ({
          subcategory: key2 ?? "Undefined",
          emissions_mean: value
        }))
      })
    )
  );
});


```
```js
const p11 ={
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
const groupedDataData = FileAttachment("p3_groupedData2.json").json();
```

```js
const p12 = {
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




```js
const p3 = {
  marks: [
    Plot.barX(byQualification, { 
      y: "qualificacio_demissions_de_co2",
      x: "ratio",                      
      fill: "green"                 
    })
  ]
};
```
```js
const groupedData22 = FileAttachment("p3_groupedData2.json").json();
```

<div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 100%;">
  <h2>Quins tipus d’edificis generen més emissions?</h2>
  <p>Comparant emissions segons la seva qualificació energètica, tipus de normativa, aïllament..</p>
  <div style="display: flex; width: 100%; align-items: center;">
    <div style="width: 53%; min-height: 400px;">${Plot.plot(p11)}</div>
    <div style="width: 47%; min-height: 450px;">${Plot.plot(p12)}</div>
  </div>
  <p>Les emissions dels habitatges estan fortament influenciades per la seva qualificació energètica, on els edificis amb categoria "A" són els menys contaminants i els de "G" els més contaminants, degut a la seva menor eficiència i pitjor aïllament tèrmic.</p>

<p>Pel que fa al tipus d’habitatge, els edificis terciaris (oficines, comerços, serveis) són més eficients perquè comparteixen recursos, mentre que els unifamiliars tenen més superfícies exposades i major pèrdua energètica. Un bon aïllament i finestres gruixudes ajuden a reduir el consum energètic i les emissions.</p>

<p>Finalment, la normativa afecta les emissions segons l’antiguitat dels edificis. Les construccions de 1979 són les més contaminants per tenir menys exigències d’eficiència, mentre que les més recents (2006, 2013 i 2019) han millorat gràcies a regulacions més estrictes que fomenten materials i tècniques constructives més sostenibles.</p>
<h3>Ratio energia / emissions per qualificació.</h3>
<div style="width: 100%; min-height: 400px;">${Plot.plot(p3)}</div>
</div>




```js
const p41 = {
  x: { 
    label: "Tecnologia", 
    domain: tecnologies_ef.sort((a, b) => b.reduccio_total_co2 - a.reduccio_total_co2).map(d => d.tecnologia) 
  },
  y: { 
    label: "Reducció Total CO₂ (Kg)", 
    grid: true,
    domain: [0, Math.max(...tecnologies_ef.map(d => d.reduccio_total_co2)) * 1.1]
  },
  marginLeft: 60,
  marginTop: 50,
  marks: [
    Plot.barY(tecnologies_ef, { 
      x: "tecnologia", 
      y: "reduccio_total_co2", 
      fill: "tecnologia", 
      tip: true  
    }),
    Plot.text(tecnologies_ef, { 
      x: "tecnologia", 
      y: "reduccio_total_co2", 
      text: d => d.reduccio_total_co2.toFixed(1), 
      dy: -15,
      fill: "black", 
      fontWeight: "bold"
    })
  ]
};
```

```js
const p42 = {
  x: { 
    label: "Tecnología", 
    domain: tecnologies_ef.sort((a, b) => b.eficiencia_co2_per_euro - a.eficiencia_co2_per_euro).map(d => d.tecnologia) 
  },
  y: { 
    label: "Eficiencia CO₂ por Euro (Kg/1000 euro)", 
    grid: true,
    domain: [0, Math.max(...tecnologies_ef.map(d => d.eficiencia_co2_per_euro)) * 1.1] 
  },
  marginLeft: 60,  
  marginTop: 50,   
  marks: [
    Plot.barY(tecnologies_ef, { 
      x: "tecnologia", 
      y: "eficiencia_co2_per_euro", 
      fill: "tecnologia", 
      tip: true  
    }),
    
    Plot.text(tecnologies_ef, { 
      x: "tecnologia", 
      y: "eficiencia_co2_per_euro", 
      text: d => d.eficiencia_co2_per_euro.toFixed(2), 
      dy: -15, 
      fill: "black", 
      fontWeight: "bold"
    }),
  ]
};
```

<div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 100%;">
  <h2>Quines polítiques o intervencions resulten més eficients en termes de reducció d’emissions per euro invertit?</h2>
  <p>Anàlisi de tecnologies per reduir emissions de CO₂: vehicles elèctrics, xarxa de districte, biomassa i energia geotèrmica.</p>
  <div style="display: flex; width: 100%; align-items: center;">
    <div style="width: 48%; min-height: 400px;">${Plot.plot(p41)}</div>
    <div style="width: 52%; min-height: 450px;">${Plot.plot(p42)}</div>
  </div>
  <p>Per determinar quina tecnologia ofereix una millor relació entre la reducció total de CO₂ i el cost d’instal·lació, s’ha calculat la diferència entre les emissions de referència (edificis sense aquestes tecnologies) i les emissions reals dels edificis que les utilitzen.</p>

  <p>La reducció total de CO₂ per tecnologia es calcula sumant la reducció individual de tots els edificis que utilitzen cada tecnologia. Això ens permet veure quina tecnologia té un major impacte absolut en la reducció d’emissions.</p>

  <p>Per entendre la relació entre la reducció d’emissions i el cost, hem calculat l’eficiència de reducció de CO₂, definida com la relació entre la reducció d'emissions totals i el cost de la tecnologia corresponent, en kg/1000€. El cost establert han sigut estimacions de la mitjana del cost d'instalació de cada una de les tecnologies.</p>

  <p>Els resultats mostren diferències significatives entre les tecnologies analitzades, destacant aquelles que ofereixen el millor rendiment en termes d’eficiència i inversió econòmica.</p>
</div>


## Com es poden identificar els edificis amb el màxim potencial de reducció d’emissions?

L'objectiu d'aquests gràfics és clar: *trobar els edificis que, dins de cada categoria de qualificació d’emissions de CO₂, tenen més marge de millora en eficiència energètica*.  

Cada gràfic representa una qualificació d'*emissions de CO₂*, i dins de cada un volem identificar els edificis que compleixen dos criteris clau:  

1. *Ràtio d'eficiència més baix*  
   - Un ràtio d'eficiència alt significa que l’edifici té un bon rendiment energètic.  
   - Busquem els edificis amb un ràtio més baix dins de cada qualificació, ja que són els menys eficients i tenen més marge de millora.  

2. *Consum energètic per metre quadrat elevat*  
   - Un consum més alt per m² indica que l’edifici gasta molta energia en relació amb la seva mida.  
   - Aquests edificis són els que podrien beneficiar-se més de millores en eficiència energètica.  

Volem trobar els edificis que, *dins de la seva qualificació d’emissions de CO₂, estan rendint per sota del que s’espera*.  
Aquests edificis representen oportunitats clares de millora perquè:  

- *Consumeixen més energia de la que haurien de consumir* per la seva categoria.  
- *Poden beneficiar-se d’intervencions* com millores en aïllament, optimització de sistemes de climatització o implementació de tecnologies més eficients.  
- *Reduir el seu consum energètic tindria un impacte positiu* tant en costos com en sostenibilitat.  
 
- *Els punts més grans representen els edificis amb un consum per m² més alt*, fet que els converteix en candidats ideals per a l'optimització.  
- *Ens centrem en els punts amb un ràtio d'eficiència més baix i un consum alt*, ja que són els que més poden millorar.  
- *Comparar dins de cada qualificació ens permet entendre quins edificis estan per sota del que s'espera i requereixen intervenció*.

```js
const scatter_q32 = FileAttachment("scatter_q3-2.csv").csv({typed: true});
```
```js
const qualificacions = Array.from(new Set(scatter_q32.map(d => d.qualificacio_demissions_de_co2)));
const filtroQualificacio = view(Inputs.select(qualificacions, { label: "Selecciona qualificació CO₂" }));
const filtered_scatter_q3 = scatter_q32.filter(d => d.qualificacio_demissions_de_co2 === filtroQualificacio);
const sampled_scatter_q3 = filtered_scatter_q3.filter(() => Math.random() < 0.5);
```


```js
const pyoquese = {
  width: 700,
  height: 500,
  marginTop: 50,  // Espacio extra para el título
  marginBottom: 50,  // Espacio para el eje X
  x: { label: "Consumo energético por m² (kWh/m²)" },
  y: { label: "Ratio de eficiencia energética" },
  color: {
    type: "linear",
    domain: [
      Math.min(...sampled_scatter_q3.map(d => d.ratio_eficiencia)), 
      Math.max(...sampled_scatter_q3.map(d => d.ratio_eficiencia))
    ],
    range: ["red", "blue"],
    legend: true,  // Agregar leyenda
    label: "Ratio de eficiencia (bajo → alto)"
  },
  marks: [
    // Título del gráfico
    Plot.text([{}], {
      x: 0.5, y: 1.05, text: "Relación entre Consumo y Eficiencia Energética",
      frameAnchor: "top", fontSize: 18, fontWeight: "bold"
    }),
    // Subtítulo
    Plot.text([{}], {
      x: 0.5, y: 1.02, text: "Colores de rojo (ineficiente) a azul (eficiente) - Tamaño según consumo",
      frameAnchor: "top", fontSize: 14, fill: "gray"
    }),
    // Scatter plot con puntos estilizados
    Plot.dot(filtered_scatter_q3, { 
      x: "consum_m2", 
      y: "ratio_eficiencia", 
      fill: "ratio_eficiencia", 
      r: d => Math.sqrt(d.consum_m2) * 6, // Tamaño de puntos basado en consumo_m2
      opacity: 0.8
    })
  ],
  style: {
    fontFamily: "Arial, sans-serif"
  }
};
```

<div style="display: flex; flex-direction: column; align-items: center; text-align: center; width: 100%;">
  <h2>Quines polítiques o intervencions resulten més eficients en termes de reducció d’emissions per euro invertit?</h2>
  <div style="display: flex; width: 100%; align-items: center;">
    <div style="width: 100%; min-height: 400px;">${Plot.plot(pyoquese)}</div>
  </div>
  <p>Per determinar quina tecnologia ofereix una millor relació entre la reducció total de CO₂ i el cost d’instal·lació, s’ha calculat la diferència entre les emissions de referència (edificis sense aquestes tecnologies) i les emissions reals dels edificis que les utilitzen.</p>

  <p>La reducció total de CO₂ per tecnologia es calcula sumant la reducció individual de tots els edificis que utilitzen cada tecnologia. Això ens permet veure quina tecnologia té un major impacte absolut en la reducció d’emissions.</p>

  <p>Per entendre la relació entre la reducció d’emissions i el cost, hem calculat l’eficiència de reducció de CO₂, definida com la relació entre la reducció d'emissions totals i el cost de la tecnologia corresponent, en kg/1000€. El cost establert han sigut estimacions de la mitjana del cost d'instalació de cada una de les tecnologies.</p>

  <p>Els resultats mostren diferències significatives entre les tecnologies analitzades, destacant aquelles que ofereixen el millor rendiment en termes d’eficiència i inversió econòmica.</p>
</div>