export default {
  title: "Hackató 2025",
  head: `
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hackató Màster en Ciència de Dades UdG 2025</title>
  <meta name="description" content="Aquesta hackató és una activitat compartida entre les assignatures de Gestió de Projectes en Ciència de Dades i Visualització de l'Informació del Màster de Ciència de Dades de la Universitad de Girona. Amb el suport de la ViT Foundation, la Càtedra Lluís Santaló d'Aplicacions de la Matemàtica i la Càtedra d'Informació i Computació (Eurecat).">
  <meta name="keywords" content="Catalunya, dades obertes, visualització de dades, ciència de dades, Observable Framework">
  <meta name="author" content="Universitat de Girona">
  <meta property="og:title" content="Hackató Màster en Ciència de Dades UdG 2025">
  <meta property="og:description" content="Aquesta hackató és una activitat compartida entre les assignatures de Gestió de Projectes en Ciència de Dades i Visualització de l'Informació del Màster de Ciència de Dades de la Universitad de Girona. Amb el suport de la ViT Foundation, la Càtedra Lluís Santaló d'Aplicacions de la Matemàtica i la Càtedra d'Informació i Computació (Eurecat).">
  <meta property="og:type" content="website">
  <meta property="og:url" content="">
  <meta property="og:image" content="">
  <meta name="twitter:card" content="">
  <meta name="twitter:title" content="Hackató Màster en Ciència de Dades UdG 2025">
  <meta name="twitter:description" content="Aquesta hackató és una activitat compartida entre les assignatures de Gestió de Projectes en Ciència de Dades i Visualització de l'Informació del Màster de Ciència de Dades de la Universitad de Girona. Amb el suport de la ViT Foundation, la Càtedra Lluís Santaló d'Aplicacions de la Matemàtica i la Càtedra d'Informació i Computació (Eurecat).">
  <meta name="twitter:image" content="/docs/img/social.png">
  <link rel="shortcut icon" type="image/x-icon" href="">
  <link rel="preconnect" href="https://use.typekit.net" crossorigin />
  <link rel="preconnect" href="https://p.typekit.net" crossorigin />
  <link rel="preload" as="style" href="https://use.typekit.net/vpz4xzt.css" />
  <link rel="stylesheet" href="https://use.typekit.net/vpz4xzt.css" media="print" onload="this.media='all'" />
  <link rel="stylesheet" href="styles.css">
  <noscript>
    <link rel="stylesheet" href="https://use.typekit.net/vpz4xzt.css" />
  </noscript>
  `,
  search: false,
  pages: [
    {
      name: "Documentació",
      path: "/docs/",
      open: true,
      pages: [
        {name: "L'activitat", path: "/docs/"},
        {name: "Per on començar", path: "/docs/pages/comencar"},
        {name: "Exemples de codi", path: "/docs/pages/tecniques"},
        {name: "Una petita guia", path: "/docs/pages/guia"}
      ]
    },
    {
      name: "Dades",
      path: "/dades/",
      open: true,
      pages: [
        {name: "Font i dades", path: "/dades/"},
      ]
    },
    {
      name: "Projectes",
      path: "/projectes/",
      open: true,
      pages: [
        {name: "Donicelas",
          path: "/projectes/donicelas/",
        },
        {name: "Raposos",
          path: "/projectes/raposos/",
        },
        {name: "Teixugos",
          path: "/projectes/teixugos/",
        },
        {name: "Xabaríns",
          path: "/projectes/xabarins/",
        }
      ]
    }
  ],
  header:`<style>

  #observablehq-header .logo {
    height: 2rem;
    width: auto;
  }

  #observablehq-header a[href] {
    color: inherit;
  }
  
  #observablehq-header a[target="_blank"] {
    display: flex;
    align-items: center;
    gap: 0.25rem;
    text-decoration: none;
  }
  
  #observablehq-header a[target="_blank"]:hover span {
    text-decoration: underline;
  }
  
  #observablehq-header a[target="_blank"]:not(:hover, :focus)::after {
    color: var(--theme-foreground-muted);
  }
  
  @container not (min-width: 640px) {
    .hide-if-small {
      display: none;
    }
  }
  
  </style>`,
  root: "src",
  style:"style.css",
  // Some additional configuration options and their defaults:
  // theme: "default", // try "light", "dark", "slate", etc.
  // footer: "Built with Observable.", // what to show in the footer (HTML)
  // sidebar: true, // whether to show the sidebar
  // toc: true, // whether to show the table of contents
  pager: false, // whether to show previous & next links in the footer
  // output: "dist", // path to the output root for build
  // search: true, // activate search
  // linkify: true, // convert URLs in Markdown to links
  typographer: true, // smart quotes and other typographic improvements
  footer: ''
};
