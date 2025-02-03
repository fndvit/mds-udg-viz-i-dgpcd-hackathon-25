---
title: Per on començar
toc: true
---

# Per on començar
El [projecte el tenim a *GitHub*](https://github.com/fndvit/mds-udg-viz-i-dgpcd-hackathon-25), per col·laborar eficaçment.

1. Clona el [projecte](https://github.com/fndvit/mds-udg-viz-i-dgpcd-hackathon-25).
2. Entra a la carpeta que s'ha clonat.
3. Instal·la el projecte amb `npm i`.
4. I executa `npm run dev`.

Veuràs aixó ...

<pre class="observablehq-pre-container" data-copy="none"><b class="green">Observable Framework</b> v1.13.2
↳ <u><a href="http://127.0.0.1:3000/" style="color: inherit;">http://127.0.0.1:3000/</a></u></pre>

## Estructura del projecte

```
.
├─ src
│  ├─ docs
│  ├─ dades
│  │     ├─ font
│  │     └─ final
│  ├─ projectes
│  │  ├─ donicelas
│  │  │  ├─ dades
│  │  │  │  ├─ data-a.json
│  │  │  │  ├─ data-b.json
│  │  │  │  ├─ mapa.json
│  │  │  │  └─ ...
│  │  │  └─ index.md
│  │  ├─ raposos
│  │  │  ├─ dades
│  │  │  │  ├─ data-a.json
│  │  │  │  ├─ data-b.json
│  │  │  │  ├─ mapa.json
│  │  │  │  └─ ...
│  │  │  └─ index.md
│  │  └─ ...
│  └─ ...
└─ ...
```

## Recomanacions de col·laboració
- Feu servir carpetes i noms de fitxers llegibles per humans per facilitar la identificació del contingut. Preferiu fitxers en minúscules separats per guions. Ex: `ine-variables-dictionary.json`
- Seguiu el model **Branch-per-feature**: una funcionalitat, una branca.
- Precediu cada branca amb el nom del vostre equip. Ex: si esteu netejant les dades, pugeu-ho a la branca `donicelas/data-cleaning`.
- Utilitzeu un patró coherent per als missatges de commit. Un bon format és fer una descripció de la tasca en mode imperatiu `refactor: use map instead of for loop`

## Un resum del procés

- **Clona i instal·la el repositori**
- **Canvia a la branca primària del teu projecte** 
- **Crea una branca per a la teva feature**: Abans de fer cap canvi extra, crea una nova branca per a la teva *feature* seguint [l'estructura que vam explicar a dalt](#recomanacions-de-collaboracio).
- **Fes els teus canvis i fes *commit*:** Fes els canvis necessaris al codi i fes un commit amb un missatge descriptiu.
- **Puja els canvis a GitHub**
- **Crea una *pull request* cap la teva branca de projecte:** Ves al repositori a GitHub i crea una PR des de la teva branca —on has implementat la teva *feature*— cap a la branca primària del teu projecte.

Us recomanem fer servir [*GitHub Desktop*](https://desktop.github.com/) per gestionar l'accés al repositori o directament des de [*Visual Studio Code*](https://code.visualstudio.com/docs/sourcecontrol/github).