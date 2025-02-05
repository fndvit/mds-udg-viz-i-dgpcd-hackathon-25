# Raposos: Dataset Documentation

# Introducció

El grup de Raposos ha de respondre a la pregunta **"És possible dissenyar estratègies que maximitzin l’estalvi i alhora redueixin les desigualtats?"**. Després de veure les dades disponibles, creiem que sí que és possible. 
Proposem resoldre aquesta pregunta mitjançant les dades que se'ns han proporcionat inicialment a **certificats.csv**, per tenir informació relacionada amb els consums d'energia de cada edifici. També tindrem en compte altres característiques que ens puguin donar pistes sobre el per què d'aquest consum, com per exemple els nivells d'aïllament (transmitància) de l'edifici o la presència d'instal·lacions que permetin generar energia renovable i disminuir el consum.
Per tractar el tema de les desigualtats, hem agafat dades de l'Institut Nacional d'Estadística (INE), que ens permetran relacionar, per cada secció censal, els nivells de renda i de pobresa, entre altres mètriques, amb els nivells de consum i d'eficiència energètica.
Un punt important és que el dataset estarà filtrat per aquells edificis que siguin utilitzats principalment com a habitatges, és a dir, **edifics d'ús residencial**, deixant de banda edificis que la seva funció sigui qualsevol altre, com per exemple oficines. Hem pres aquesta decisió perquè, si bé és important que l'eficiència energètica sigui present a tot arreu, creiem que és coherent enfocar el tema de les desigualtats econòmiques cap a les llars de les famílies.

## Estructura del Dataset  

A continuació es descriuen les columnes que utilitzarem, extretes del dataset de **certificats.csv** (1-6) i de l'INE (7):

### **1. Identificació i Ubicació**  
- `mundissec`: Identificador únic de la secció censal on es troba l'edifici.  
- `zona_climatica`: Zona climàtica segons DB H1 del Codi Tècnic d’Edificació.  
- `any_construccio`: Any de construcció de l'edifici.  
- `us_edifici`: Ús de l’edifici (habitatge, terciari).  

### **2. Eficiència i Consum Energètic**  
- `energia_prim_ria_no_renovable`: Valor d’energia primària no renovable [kWh/m²·any].  
- `consum_d_energia_final`: Energia en el punt de consum equivalent al consum energètic [kWh/m²·any].  
- `cost_anual_aproximat_d_energia`: Cost anual aproximat d’energia per habitatge.  

### **3. Fonts d’Energia Renovable**  
- `vehicle_electric`: Disposa de punt de recàrrega de vehicle elèctric (Sí/No).  
- `solar_termica`: Disposa d’instal·lació solar tèrmica (Sí/No).  
- `solar_fotovoltaica`: Disposa d’instal·lació fotovoltaica (Sí/No).  
- `sistema_biomassa`: Disposa d’instal·lació de biomassa (Sí/No).  
- `xarxa_districte`: Disposa de connexió a una xarxa de districte de generació de calor i/o fred (Sí/No).  
- `energia_geotermica`: Disposa d’instal·lació geotèrmica (Sí/No).  

### **4. Aïllament i Ventilació**  
- `valor_aillaments`: Transmitància mitjana de façana [W/m²·K].  
- `valor_finestres`: Transmitància mitjana de finestres [W/m²·K].  
- `ventilacio_us_residencial`: Taxa de ventilació per a ús residencial [ren/h].  

### **5. Distribució del Consum Energètic**  
- `energia_calefacci`: Consum d’energia primària no renovable pel servei de calefacció [kWh/m²·any].  
- `energia_refrigeraci`: Consum d’energia primària no renovable pel servei de refrigeració [kWh/m²·any].  
- `energia_acs`: Consum d’energia primària no renovable pel servei d’ACS [kWh/m²·any].  
- `energia_enllumenament`: Consum d’energia primària no renovable pel servei d’il·luminació [kWh/m²·any].  

### **6. Rehabilitació i Millores Energètiques**  
- `rehabilitacio_energetica`: S’ha realitzat una rehabilitació energètica (Sí/No).  
- `actuacions_rehabilitacio`: Actuacions de la rehabilitació.  

### **7. Dades Econòmiques i Demogràfiques**  
- `codi_districte`: Codi que identifica el districte administratiu.  
- `codi_postal`: Codi postal de la localitat.  
- `poblacio`: Nom del municipi o població.  
- `year`: Any de la dada o registre.  
- `renta_neta_mitja_por_persona`: Renda neta mitjana per persona [€].  
- `renta_neta_mitja_por_hogar`: Renda neta mitjana per hogar [€].  
- `renta_mitja_por_unitat_consum`: Renda mitjana per unitat de consum [€].  
- `renta_mediana_por_unitat_consum`: Renda mediana per unitat de consum [€].  
- `renta_bruta_mitja_por_persona`: Renda bruta mitjana per persona [€].  
- `renta_bruta_mitja_por_hogar`: Renda bruta mitjana per llar [€].  
- `renta_bruta_mitja_por_persona_fuente_salario`: Renda bruta mitjana per persona provinent de salari [€].  
- `renta_bruta_mitja_por_persona_fuente_pensiones`: Renda bruta mitjana per persona provinent de pensions [€].  
- `renta_bruta_mitja_por_persona_fuente_desempleo`: Renda bruta mitjana per persona provinent d'atur [€].  
- `renta_bruta_mitja_por_persona_fuente_otras_prestaciones`: Renda bruta mitjana per persona provinent d'altres prestacions [€].  
- `renta_bruta_mitja_por_persona_fuente_otros_ingresos`: Renda bruta mitjana per persona provinent d'altres ingressos [€].  
- `indice_gini`: Índex de Gini, mesura de la desigualtat de la distribució de la renda (0 = igualtat perfecta, 1 = desigualtat total).  
- `distribucion_renta_p80_p20`: Distribució de la renda entre el percentil 80 i el percentil 20 (mesura de desigualtat relativa).  
- `edad_media_poblacion`: Edat mitjana de la població.  
- `prcnt_poblacion_menor_edad`: Percentatge de la població menor d'edat.  
- `prcnt_poblacion_mas_65_anos`: Percentatge de la població de més de 65 anys.  
- `tamano_medio_hogar`: Mida mitjana de la llar (número d'individus per llar).  
- `prcnt_hogares_unipersonales`: Percentatge de llars unipersonals.  
- `poblacion_habitantes`: Nombre total d'habitants de la població.  
- `prcnt_poblacion_espanola`: Percentatge de la població que és de nacionalitat espanyola.  

