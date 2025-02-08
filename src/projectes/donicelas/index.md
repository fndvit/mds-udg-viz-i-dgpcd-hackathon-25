```js
import * as d3 from "npm:d3";
import {sankey, sankeyLinkHorizontal} from "d3-sankey"
```

```js
const comarques_municipis_catalunya = FileAttachment("data/comarcas_municipis.json").json();
const media_eff_energetica = FileAttachment("data/media_eff_energetica.json").json();
const renta_merged_percapita = FileAttachment("data/renta_merged_percapita.json").json();
const links = FileAttachment("data/sankey3.csv").csv();
const me_boxplot_data = FileAttachment("data/ME_boxplot_data.csv").csv();
````
```js
const nodes = Array.from(new Set(links.flatMap(l => [l.source, l.target])), name => ({name, category: name.replace(/ .*/, "")}));
```
```js
const nodes = Array.from(new Set(links.flatMap(l => [l.source, l.target])), name => ({name, category: name.replace(/ .*/, "")}));
const data = {nodes, links};
console.log(sankey)
```



```js
const comarques_map =  comarques_municipis_catalunya['comarques'];
const municipis_map =  comarques_municipis_catalunya['municipis'];
const media_eff_municipis_map = Object.fromEntries(media_eff_energetica.map(row => Array(row['codi_municipi'], row['energy_middle'])));
console.log(media_eff_municipis_map)

````

```js
const linkColorInput = Inputs.select(new Map([
    ["static", "#aaa"],
    ["source-target", "source-target"],
    ["source", "source"],
    ["target", "target"],
]), {
    value: new URLSearchParams(html`<a href>`.search).get("color") || "source-target",
    label: "Link color"
});
```
```js
const linkColor = Generators.input(linkColorInput);
```

```js
const to_color_effi = (effi) => {
    if (effi < 25) {
        return "#00792C";
    }else{
        if (effi < 50) {
            return "#00A246";
        }else{
            if (effi < 75) {
                return "#97BE0D";
            }else{
                if (effi < 100) {
                    return "#FFCC00";
                }else{
                    if (effi < 125) {
                        return "#F7B261";
                    }else{
                        if (effi < 150) {
                            return "#EC7E00";
                        }else{
                            return "#E2001A";
                        }
                    }
                }
            }
        }
    }
}
const plot_catalunya_municipi = (width) => {
    return Plot.plot({
        projection: {
            type: "conic-conformal",
            domain: comarques_map
        },
        color: {
            type: "threshold",
            range: ["#00792C",
                "#00A246",
                "#97BE0D",
                "#FFCC00",
                "#F7B261",
                "#EC7E00",
                "#E2001A"],
            legend: true,
            pivot: 17.96,
            n: 10,
            unknown: "black",
            domain: [12, 38, 63, 88, 113, 138, 163],
            label: "Població de 65 anys i més (%)",
        },
        width: width,
        marks: [
            Plot.geo(municipis_map, {
                fill: (d) => media_eff_municipis_map[d.properties.CODIMUNI],
                strokeOpacity: 1.0,
                strokeWidth: 1,
                stroke: "black",
                tip: true
            }),
            Plot.geo(comarques_map, {
                strokeOpacity: 1.0,
                strokeWidth: 2,
                stroke: "black",
                tip: true
            })
        ]
    });
};

```

```js
const plot_bubble = (width) => {
    return Plot.plot({
        width,
        height: 600,
        x: {
            ticks: [],
            label: "Renda per persona mitjana",
            domain: [10, 25]
        },
        y: {
            ticks: [],
            label: "Qualificació energètica mitjana",
            domain: [40, 90],
        },
        marks: [
            Plot.circle(renta_merged_percapita, {
                x: (d) => parseFloat(d.renta),
                y: (d) => parseFloat(d.qualificacio),
                r: (d) => d.cens,
                fill: (d) => {
                    const qualificacio = parseFloat(d.qualificacio);
                    if (qualificacio <= 25) return "darkgreen";      // 0-25 -> verd fosc
                    if (qualificacio <= 50) return "green";          // 26-50 -> verd
                    if (qualificacio <= 75) return "lightgreen";     // 51-75 -> verd fluix
                    if (qualificacio <= 100) return "yellow";        // 76-100 -> groc
                    if (qualificacio <= 125) return "lightorange";   // 101-125 -> taronja fluix
                    if (qualificacio <= 150) return "orange";        // 126-150 -> taronja
                    return "red";                                    // >150 -> vermell
                },
                stroke: "black",
                strokeWidth: 1,
                title: (d) => `${d.poblacio}`,
                tip: true,
            }),

        ]
    })
}

```
```js
const plot_relation = (width) => {
    // Specify the dimensions of the chart.
    const height = 600;
    const format = d3.format(",.0f");

    // Create a SVG container.
    const svg = d3.create("svg")
        .attr("width", width)
        .attr("height", height)
        .attr("viewBox", [0, 0, width, height])
        .attr("style", "max-width: 100%; height: auto; font: 10px sans-serif;");

    // Constructs and configures a Sankey generator.
    const sankey2 = sankey()
        .nodeId(d => d.name)
        .nodeAlign(d3["center"]) // Asegura la alineación
        .nodeWidth(15)
        .nodePadding(10)
        .nodeSort((a, b) => {
            const order = { "Classe Alta": 0, "Classe Media": 1, "Classe Baja": 2 };
            return order[a.name] - order[b.name];
        })
        .extent([[1, 5], [width - 1, height - 5]]);

    // Applies it to the data. We make a copy of the nodes and links objects
    // so as to avoid mutating the original.

    const {nodes, links} = sankey2({
        nodes: data.nodes
            .map(d => Object.assign({}, d))
            .sort((a, b) => {
                const order = { "Classe Alta": 0, "Classe Media": 1, "Classe Baja": 2 };
                return order[a.name] - order[b.name];
            }),
        links: data.links.map(d => Object.assign({}, d))
    });

    // Defines a color scale.
    const color = d3.scaleOrdinal(d3.schemeCategory10);

    // Creates the rects that represent the nodes.
    const rect = svg.append("g")
        .attr("stroke", "#000")
        .selectAll()
        .data(nodes)
        .join("rect")
        .attr("x", d => d.x0)
        .attr("y", d => d.y0)
        .attr("height", d => d.y1 - d.y0)
        .attr("width", d => d.x1 - d.x0)
        .attr("fill", d => color(d.category));

    // Adds a title on the nodes.
    rect.append("title")
        .text(d => `${d.name}\n${format(d.value)} TWh`);

    // Creates the paths that represent the links.
    const link = svg.append("g")
        .attr("fill", "none")
        .attr("stroke-opacity", 0.5)
        .selectAll()
        .data(links)
        .join("g")
        .style("mix-blend-mode", "multiply");

    link.append("path")
        .attr("d", sankeyLinkHorizontal())
        .attr("stroke", d => color(d.target.category))
        .attr("stroke-width", d => Math.max(1, d.width));

    link.append("title")
        .text(d => `${d.source.name} → ${d.target.name}\n${format(d.value)} TWh`);

    // Adds labels on the nodes.
    svg.append("g")
        .selectAll()
        .data(nodes)
        .join("text")
        .attr("x", d => d.x0 < width / 2 ? d.x1 + 6 : d.x0 - 6)
        .attr("y", d => (d.y1 + d.y0) / 2)
        .attr("dy", "0.35em")
        .attr("text-anchor", d => d.x0 < width / 2 ? "start" : "end")
        .text(d => d.name);

    return svg.node();
}
```

# Energy efficiency by district. - MDS Hackathon 2025

## Donicelas Team

Is energy efficiency evenly distributed across Catalonia?

Suppose that older buildings in areas with lower incomes tend to have worse ratings, while urban districts with greater economic resources have more efficient buildings. This inequality can have significant implications for social equity and public policy.


## Objectives
Identify correlations between energy efficiency ratings and socioeconomic variables such as income, housing age and degree of urbanisation.
Develop tools to help policy makers design regulatory subsidies and incentives that target regions with the worst energy efficiency performance.
Prioritise the renovation of social housing as a key measure to improve efficiency and reduce inequalities.
Visualizations of the impact on energy efficiency according to different socioeconomic levels in Catalonia


1. Which municipalities in Catalonia have the highest and lowest average energy efficiency?
   Visualization:
   Heat map of Catalonia (Average energy efficiency by municipality)

<div class="grid grid-cols-4">
    <div class="card grid-colspan-2">
        <h2>Municipis</h2>
        <figure class="grafic" style="max-width: none;">
            ${resize((width) => plot_catalunya_municipi(width))}
        </figure>
    </div>
 

</div>

   Ranking bar chart (Energy efficiency score by municipality)
   <img src="/img/barchart.png" alt="Description of Image" width="800">

   Bubble chart (Energy rating - population vs. income)

<div class="grid grid-cols-4">
   <div class="card grid-colspan-2">
        <h2>Per capita</h2>
        <figure class="grafic" style="max-width: none;">
            ${resize((width) => plot_bubble(width))}
        </figure>
    </div>
    <div class="card grid-colspan-2">
        <h2>Relaciones</h2>
        <figure class="grafic" style="max-width: none;">
            ${resize((width) => plot_relation(width))}
        </figure>
    </div>
</div>
<img src="/img/relations.png" alt="Description of Image" width="800">
    


2. How does the level of income in different areas affect the energy efficiency of homes?
   Visualization:
   SANKEY diagram (Income level and energy efficiency)

3. Do urban areas have higher energy efficiency compared to rural areas?
   Visualization:
   Boxplot  (Energy Efficiency by Rural or Urban)
   <img src="/img/boxplot_me.png" alt="Description of Image" width="800">


4. ¿Cómo utilizar estos datos para orientar las políticas de subvenciones e incentivos?
   By analyzing energy efficiency across municipalities, income levels, and urban-rural differences, policymakers can allocate subsidies and incentives to low-income areas and regions with poor energy efficiency, ensuring targeted improvements and equitable distribution of resources.





## Most important challenges

1. Finding relevant data:
   Challenge: It was difficult to find a complete data set on energy efficiency in Catalonia. The data was fragmented in different sources and there was a blockage of access to cadastral data due to excessive attempts.
   Solution: Use the energy efficiency register of the Catalan Energy Institute (ICAEN) and cross-reference it with data from the Statistics Institute of Catalonia (Idescat). This allowed a more complete data set to be built.

2. Connecting socioeconomic and energy data:
   Challenge: Socioeconomic data and energy efficiency records were not aligned by a single common identifier, such as the municipality.
   Solution: Manually map geographic identifiers and use tools such as Python.

3. Visualization of results:
   Challenge: Visually represent the inequalities in energy efficiency in Catalonia due to the high number of variables and the large number of alternatives to visualize the data.
   Solution: Use visualization libraries such as Plot to create interactive maps.

4. Lack of updated or complete data
   Challenge: Records were outdated or incomplete in some municipalities.
   Solution: Work with data with similar characteristics in neighboring areas.

5. Time constraints
   Challenge: Complete an extensive analysis in a short time, such as in a hackathon.
   Solution: Divide the work into subteams with specific tasks.

We have managed to make progress with some graphs and analysis, but we still have to do:

1. Develop an analytical/predictive model
   • Predict the energy rating of a home or identify priority areas for interventions.
   • Select the key variables (income, age, urbanization, size of the home).
   • Train a model such as linear regression, decision trees or neural networks.
   • Evaluate performance with metrics such as MAE, RMSE, or precision.

2. Go deeper into statistical analysis
   • Validate and reinforce the conclusions with detailed analysis, through cluster identification with techniques such as K-means or principal component analysis (PCA).

3. Evaluate the social impact
   • Propose metrics to measure how the interventions will reduce inequalities.
   • Some suggested metrics:
   o Reduction of CO2 emissions.
   o Increase in average energy ratings in vulnerable areas.
   o Number of homes rehabilitated in low-income areas.



