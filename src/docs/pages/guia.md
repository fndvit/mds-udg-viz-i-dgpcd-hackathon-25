---
title: Una petita guia
toc: false
---

<style>
.example { position: relative; }

.example::after {
  position: absolute;
  top: .5rem;
  right: 1rem;
  font-size: 1.5rem;
}

.right::after {
  content: '\2714';
  color: var(--theme-foreground-focus);
}

.wrong::after {
  content: '\2718';
  color: var(--theme-foreground-faint);
}

.hm::after {
  content: '\1F914';
}

.happy::after {
  content: '\1F60A';
}

.nopad {
  padding-top: 0;
  margin-top: 0;
}

.caption {
  font-size: .8rem;
  line-height: 1.35;
  font-family: var(--sans-serif);
  color: var(--theme-foreground-alt);
}

</style>

```js
import chroma from "npm:chroma-js";

const margarine = [8.2,7,6.5,5.3,5.2,4,4.6,4.5,4.2,3.7,];
const divorces = [5,4.7,4.6,4.4,4.3,4.1,4.2,4.2,4.2,4.1,];

const remap = d3.scaleLinear(d3.extent(divorces), d3.extent(margarine));

```

# Una petita guia d'estil
## Recomanacions pràctiques
Organitzeu la documentació i els panells de dades amb un **fluix narratiu lògic**. Comenceu amb una visió general o resum a dalt, donant context, i continueu amb la informació més detallada a sota. Això ajuda els usuaris a comprendre el context general abans d'endinsar-se en els detalls específics.

Als panells de dades, una possible estructura lògica seria:

### Títol del panell
<div class="grid grid-cols-4">
  <div class="card grid-colspan-3 grid-rowspan-4">Gràfic principal</div>
  <div class="card grid-colspan-1">Dada destacada</div>
  <div class="card grid-colspan-1">Dada destacada</div>
  <div class="card grid-colspan-1">Dada destacada</div>
  <div class="card grid-colspan-1">Dada destacada</div>
</div>
<div class="grid grid-cols-4">
  <div class="card grid-colspan-4 grid-rowspan-2">Gràfic de detall</div>
  <div class="card grid-colspan-4">Taula</div>
</div>

---
Igualment, estructureu el panell de manera que la importància visual reflecteixi la importància informativa de cada element. En general, la informació més important hauria d'estar en targetes més grans i prominents, atraient l'atenció immediata. Una **bona jerarquia visual** ajuda a guiar els usuaris intuïtivament a través del panell, millorant la seva comprensió i interacció.

---
Crideu l'atenció a les **mètriques i tendències més importants** utilitzant indicadors visuals com ara fonts en negreta o mides més grans. Destacar aquestes dades facilita que els usuaris trobin la informació clau més aviat.
<div class="grid grid-cols-4">
  <div class="card grid-colspan-1"><h1>1</h1> gat blanc i negre</div>
  <div class="card grid-colspan-1"><h1>23</h1> nenxs</div>
  <div class="card grid-colspan-1"><h1>45</h1> anys</div>
  <div class="card grid-colspan-1"><h1>6.789</h1> m³</div>
</div>

---
Eviteu sobrecarregar les targetes amb massa informació. Cada targeta ha de centrar-se en un punt únic.

---
Assegureu'vos que la **relació d'aspecte dels teus gràfics** no distorsiona els patrons de les dades. Gràfics massa amples o massa estrets poden portar a interpretacions errònies. El format 4×3 (apaïsat) o 3×4 (vertical) potser són els més comuns i prudents, però també podeu fer servir l'1×1 pels diagrames de dispersió, o formats més extrems: molt vertical si són moltes barres horitzontal apilades, molt apaïsat si és una sèrie temporal molt llarga i detallada.
<div class="grid grid-cols-4">
  <div class="card example wrong grid-colspan-3">
  ${resize((width) => 
    Plot.barY(
      penguins,
      Plot.groupX({ y: "count" }, { x: "island", fill: "species" })).plot({ width, color: { legend: true } })
  )}

  </div>
  <div class="card example right grid-colspan-1">
   ${resize((width) => 
    Plot.barY(
      penguins,
      Plot.groupX({ y: "count" }, { x: "island", fill: "species" })).plot({ width, color: { legend: true } })
  )}

  </div>
</div>

---
Col·loqueu els **filtres, desplegables i altres elements d'input dins de la mateixa targeta que el gràfic** que modifiquen. Això fa que sigui intuïtiu per als usuaris veure com la interacció amb aquests elements afecta la visualització de dades, fent l'experiència més fluida i eficient 🥰 

Els elements interactius han de tenir instruccions clares sobre el seu ús per asegurar la seva accessibilitat.

---
Cada gràfic ha de tenir **títol clar i descriptiu**, així com una **llegenda si és necessari**. Els títols ajuden els usuaris a entendre què estem mostrant, mentre que les llegendes expliquen el significat dels colors i altres elements. Aquest context és crucial per a una interpretació precisa de les dades.

Incorporar les etiquetes directament els elements gràfics permet una interpretació més intuïtiva i directa de les dades, eliminant la necessitat de cercar referències en altres parts de la visualització. Utilitzar títols descriptius ajuda els usuaris a comprendre ràpidament el contingut dels gràfics. A més, aplicar etiquetatge ARIA és essencial per garantir que les visualitzacions siguin [accessibles](https://observablehq.com/plot/features/accessibility) per a persones que utilitzen tecnologies d'assistència, proporcionant una experiència inclusiva i comprensible per a tots els usuaris.

<div class="grid grid-cols-4">
  <div class="card example hm grid-colspan-2" style="padding-top:5rem;">
    ${resize((width) => 
      Plot.plot({
        width,
        height: width / 2,
        y: {axis: "left"},
        marks: [
          Plot.axisY(remap.ticks(), {color: "red", anchor: "right", y: remap, tickFormat: remap.tickFormat()}),
          Plot.lineY(
            margarine,
            {
              y: d => d,
              x: (d, i) => new Date(i + 2000, 0, 0),
              strokeWidth: 2,
              strokeDasharray: [2,4],
              marker: "dot",
              curve: "monotone-x"
            }
          ),
          Plot.lineY(
            divorces,
            Plot.mapY((D) => D.map(remap),
            {
              y: d => d,
              x: (d, i) => new Date(i + 2000, 0, 0),
              stroke: "red",
              strokeWidth: 2,
              marker: "dot",
              curve: "monotone-x"
            })
          )
        ]
      })
      )
    }

  </div>
  <div class="card example happy grid-colspan-2">
  <h2 class="nopad">Correlació entre el consum per càpita de margarina i la taxa de divorcis a Maine, Estats Units</h2>
  ${resize((width) => 
      Plot.plot({
        width,
        height: width / 2,
        y: {axis: "left", label: "lb de margarina"},
        ariaLabel: "Correlació entre el consum per càpita de margarina i la taxa de divorcis a Maine, Estats Units",
        ariaDescription:"Dues línies superposades: una negra que mostra un consum decreixent de margarina i una altra vermella que mostra una taxa de divorcis decreixent de manera similar a Maine, Estats Units. El gràfic és una broma, una correlació espúrea.",
        marks: [
          Plot.axisY(remap.ticks(), {color: "red", anchor: "right", y: remap, tickFormat: remap.tickFormat(), label: "taxa de divorcis"}),
          Plot.lineY(
            margarine,
            {
              y: d => d,
              x: (d, i) => new Date(i + 2000, 0, 0),
              strokeWidth: 2,
              strokeDasharray: [2,4],
              marker: "dot",
              curve: "monotone-x",
            }
          ),
          Plot.lineY(
            divorces,
            Plot.mapY((D) => D.map(remap),
            {
              y: d => d,
              x: (d, i) => new Date(i + 2000, 0, 0),
              stroke: "red",
              strokeWidth: 2,
              marker: "dot",
              curve: "monotone-x",
            })
          )
        ]
      })
      )
    }
    <p class="caption">Font: Tots dos gràfics representen el mateix, una correlació aleatòria deliciosament ximple d'en Tyler Vigen</p>
  </div>
</div>

Els gràfics de dalt són una broma, ja sabeu que cal tenir compte amb les [correlacions espúries](https://www.tylervigen.com/spurious/correlation/5920_per-capita-consumption-of-margarine_correlates-with_the-divorce-rate-in-maine) (mireu el blog d'en Tyler Vigen) i, si us plau, [no feu servir doble eix](https://blog.datawrapper.de/dualaxis/).

---
**Tampoc oblideu les taules**! Són una eina molt valuosa per presentar dades de manera organitzada i accessible. Quan permeten la cerca, faciliten als usuaris trobar informació específica ràpidament, i enriquides amb *sparklines* poden proporcionar una visió ràpida de les tendències sense necessitat de gràfics separats. Són una manera alternativa per als usuaris de consumir la informació en una visualització i, en general, els lectors de pantalla naveguen més fàcilment per les taules que per les visualitzacions.

## Tipografia i edició
*Observable Framework* ja ofereix tots els elements de disseny que necessiteu per formatar el vostre panell. [Llegiu sobre això aquí.](https://observablehq.com/framework/markdown)

Els estils de lletra ja estan predefinits al projecte. (La iniciativa va de desbloquejar dades obertes mitjançant la visualització, no de genialitats tipogràfiques: no cal afegir nous tipus o estils de lletra.)

---

<h1>Títol h1</h1>

---
<h2>Títol h2</h2>

---

<h3>Títol h3</h3>

---

<h3>Títol h4</h4>

---

Text de paràgraf a l'informe

---

<div class="grid grid-cols-4">
  <div class="card grid-colspan-3">
    <h1>Títol h1 a dins d'una <em>card</em></h1>
    <h2>Subtítol h2 a dins d'una <em>card</em></h2>
    <p>Text normal</p>
    <p class="caption">Text a fonts i notes</p>
  </div>
  <div class="card grid-colspan-1"><h1>Altre h1</h1></div>
</div>
