// Importar Arquero
import * as aq from 'arquero';

// Carregar el CSV
certificats = FileAttachment("../certificats.csv").csv();

// Agrupar per 'mundissec' i calcular la mitjana de les altres variables
const groupedData = certificats
  .groupby('mundissec') // Agrupar per 'mundissec'
  .reduce((acc) => ({
    mean_emissions: acc.emissions_de_co2.mean(),
    mean_energia_primaria: acc.energia_prim_ria_no_renovable.mean(),
    mean_cost_energia: acc.cost_anual_aproximat_d_energia.mean(),
  }))
  .derive({
  });

 groupedData.toCSV();