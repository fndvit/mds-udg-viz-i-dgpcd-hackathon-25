# Report: Team Raposos 🦊

## Introduction

Our scenario deals, for the most part, with energetic eficiency and socioeconomic inequities. We want to find strategies to determine where is most efficient to make investments regarding energetic efficiency, while also helping those regions where there's more poberty, or where the wealth is not shared evenly. 

To achieve this, we want to estimate the ROI (Return Of Investment) for each zone, using metrics such as the energetic efficicency or the energy consumption of each zone. We also want to estimate the socieconomic situation of each region using metrics like the average income or the Gini index.

## Objectives & Approaches

More specifically, we want to:

- Estimate the ROI (in energy savings) for different investment strategies. For this we will:
    - Give a numeric value to each efficiency letter (From A to G).
    - Calculate the mean efficiency in each zone.
    - Ponderate it by the Gini index to take into account socioeconomical situation.
    - Display it in a map, allowing to filter by edification type.

- Develop a prioritization tool for financing energy rehabilitation, focused on buildings with the highest savings potential per euro invested. Since the data for the investment is limited we will:
    - Obtain the mean rehabilitation cost for each province
    - Obtain the mean energy savings (proportion) for each province
    - Calculate the mean ROI (savings / cost) for each province
    - Ponderate this ROI for each building by:
        - Its energetic efficiency (inversely proportional)
        - The average income of the censal district (inversely proportional)
        - The Gini index of the censal district (directly proportional)
    - Display a map and a table with these values.

- Additionally, we want to display a map simply showing the mean income and a map showing gini values, just to give some context.



