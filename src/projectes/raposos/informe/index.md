# Report: Team Raposos 🦊

## Introduction

Our scenario deals, for the most part, with energetic eficiency and socioeconomic inequities. We want to find strategies to determine where is most efficient to make investments regarding energetic efficiency, while also helping those regions where there's more poberty, or where the wealth is not shared evenly. 

To achieve this, we want to estimate the ROI (Return Of Investment) for each zone, using metrics such as the energetic efficicency or the energy consumption of each zone. We also want to estimate the socieconomic situation of each region using metrics like the average income or the Gini index.

Some more general visualizations that don't answer the question directly, but that can provide some context and insight to the general situation will also be displayed.

## Objectives & Approaches

More specifically, we want to:

- Show the mean cost and mean percentage energy savings by province. For this we will:
    - Display a card for each province with the required values.

- See the relationship between socioeconomical factors, energy efficiency qualifications and ROI (in energy savings). For this we will:
    - Show a map with the mean Gini index for each censal district.
    - Show a map with the mean income for each censal district.
    - Show a map with the mean energetic efficiency for each censal district.
        - Each efficiency (A-G) will be given a numerical value (1-7).
    - Only take into account buldings classified as housing.    

- Develop a prioritization tool for financing energy rehabilitation, focused on buildings with the highest savings potential per euro invested. Since the data for the investment is limited we will:
    - Obtain the mean rehabilitation cost for each province
    - Obtain the mean energy savings (proportion) for each province
    - Calculate the mean ROI (savings / cost) for each province
    - Ponderate this ROI for each censal district by:
        - Its average energetic efficiency of the censal district (inversely proportional)
        - The average income of the censal district (inversely proportional)
        - The average Gini index of the censal district (directly proportional)
    - Display a map with these values.
    - Generate a table with these values, in descending order.
        - There will be the function to search by postal code.
    - Again, only buldings classified as housing will be taken into account.

## Issues and Solutions

In this section we will mainly detail the issue we found when trying to develop the tool to determine the best censal districts to invest.

The issue was that we didn't have any data regarding the cost each renovation, which made it impossible to get a reliable ROI (since we don't have the investment). So, we decided to use data from the ICE (Institut Català d'Energia), which detailed the total cost for all renovation projects in each province, and the total percentage of estimated energy saving. So, to get some approximations, we divided the total cost by the number of households considered in each province to get the mean cost per province. We also used the saved energy percentage as the mean saving per province. Again, this is of course only an estimation that isn't as precise as we'd like, but since we don't have the actual data it's the best approach we found to be able to estimate the ROI. 

Then, as the previous calculations give a single ROI per province (meaning, only 4 "blocks" of ROI) and we wanted different values for each censal district, we decided to ponderate it by the districts' mean energetic efficiency, average income and average Gini index.

In summary, we first calculated the approximated the ROI for each province, and then increased the result for censal districts with lower income, lower energetic efficiency, and higher Gini index.

## Used data 

As data sources we used:
- For energy-related data:
    - certificats.csv, provided by the teachers and sourced from: https://analisi.transparenciacatalunya.cat/Energia/Certificats-d-efici-ncia-energ-tica-d-edificis/j6ii-t3w2/about_data
- For socioeconomical data:
    - INE (Institut Nacional d'Estadística) data: https://www.ine.es/dynt3/inebase/es/index.htm?padre=12385&capsel=12384
- For data regarding renovation cost and savings (per province):
    - ICE (Institut Català d'Energia) data: https://icaen.gencat.cat/es/energia/ajuts/edificis/ICAEN-Programa-de-ayudas-a-la-rehabilitacion-energetica-de-edificios-PREE/dades-obertes-tecniques-dels-ajuts-atorgats/index.html
