const RESTAURANTES = [
  {
    "nombre": "Gregorio El Pescador",
    "tipo": "Local",
    "link": "https://maps.app.goo.gl/X91t4vfH5aid7PMv6",
    "comentario": "El favorito de los locales",
    "calidad": 9.4
  },
  {
    "nombre": "Casa Domingo",
    "tipo": "Local",
    "link": "https://maps.app.goo.gl/KA7fpED4KPVp8Wfr7",
    "comentario": "Pequeño pero matón 💥",
    "calidad": 9.3
  },
  {
    "nombre": "Pizzeria Vivi",
    "tipo": "Pizza",
    "link": "https://maps.app.goo.gl/DVwEaGJX9unVstVq5",
    "comentario": "La comida aquí tiene algo especial",
    "calidad": 9.2
  },
  {
    "nombre": "Los Compadres",
    "tipo": "Local",
    "link": "https://maps.app.goo.gl/FnaqF4n8xvtgXsgy6",
    "comentario": "Si sobra algo… va para casa 😄",
    "calidad": 9.0
  },
  {
    "nombre": "La Pulperia",
    "tipo": "Tapas",
    "link": "https://maps.app.goo.gl/jWUPzceLhYkXi2C16",
    "comentario": "Salí más feliz que un niño en una tienda de caramelos 🍬",
    "calidad": 9.3
  },
  {
    "nombre": "La Marquesina",
    "tipo": "Carne / Pescado",
    "link": "https://maps.app.goo.gl/yjedwHRkX48mvF1D9",
    "comentario": "Aquí siempre aciertas",
    "calidad": 9.5
  },
  {
    "nombre": "Bronx",
    "tipo": "Hambuergueseria",
    "link": "https://maps.app.goo.gl/J7LiK8RFmdanFpKJ6",
    "comentario": "Comer bien y sin complicaciones",
    "calidad": 9.2
  },
  {
    "nombre": "Cantante",
    "tipo": "Copas y Tapas",
    "link": "https://maps.app.goo.gl/4rvgCzHfNbkc1DeP6",
    "comentario": "Aquí todo sabe mejor",
    "calidad": 9.2
  },
  {
    "nombre": "Sunset Lounge",
    "tipo": "Musica y copas",
    "link": "https://maps.app.goo.gl/pgdGPWZWmYVSjoZe9",
    "comentario": "De los que recomiendas sin dudar",
    "calidad": 9.5
  },
  {
    "nombre": "El encuentro de Avelino",
    "tipo": "Mediterrano",
    "link": "https://maps.app.goo.gl/2ytTg5wS7CHonpoi6",
    "comentario": "Comida rica, servicio rápido y sonrisa asegurada",
    "calidad": 9.3
  },
  {
    "nombre": "Canela",
    "tipo": "Comida, bebida y musica",
    "link": "https://maps.app.goo.gl/8DWpgE9hkZRRTfBy5",
    "comentario": "Para venir con hambre de verdad",
    "calidad": 9.0
  },
  {
    "nombre": "Bandido",
    "tipo": "Hamburgueseria",
    "link": "https://maps.app.goo.gl/FBsJ5yeFiG8LghMa7",
    "comentario": "Ideal para una comida sin líos",
    "calidad": 9.3
  },
  {
    "nombre": "Bagus",
    "tipo": "Un poco de todo",
    "link": "https://maps.app.goo.gl/oeeinoi97zeBFMWR7",
    "comentario": "De los que te hacen el día mejor",
    "calidad": 8.9
  },
  {
    "nombre": "Olivo Corso",
    "tipo": "Mediterraneo",
    "link": "https://maps.app.goo.gl/9yJE7cuGZKTZoNS56",
    "comentario": "Perfecto para repetir mil veces",
    "calidad": 9.1
  },
  {
    "nombre": "Bodegas Canovas",
    "tipo": "Bodega",
    "link": "https://maps.app.goo.gl/qp76F4rf17LakDLw5",
    "comentario": "Un clásico que nunca falla",
    "calidad": 9.0
  },
  {
    "nombre": "Secret Garden",
    "tipo": "Restaurante",
    "link": "https://maps.app.goo.gl/dCSkkRffcpmrKBs77",
    "comentario": "El favorito de mi abuela 👵",
    "calidad": 9.0
  },
  {
    "nombre": "5 sentidos",
    "tipo": "Arroceria",
    "link": "https://maps.app.goo.gl/FHHvRdHzmG4JCn748",
    "comentario": "Aquí se viene con hambre y se sale feliz",
    "calidad": 9.1
  },
  {
    "nombre": "Casa Naturaleza",
    "tipo": "Local",
    "link": "https://maps.app.goo.gl/HvuYK684DQqG9HU98",
    "comentario": "Una sorpresa muy agradable",
    "calidad": 9.2
  },
  {
    "nombre": "El Rincon de Juanita",
    "tipo": "Mediterraneo",
    "link": "https://maps.app.goo.gl/xCBoeBCQQXjBfDoY6",
    "comentario": "De esos sitios que repites sin pensarlo",
    "calidad": 9.4
  },
  {
    "nombre": "El Horno",
    "tipo": "Carne",
    "link": "https://maps.app.goo.gl/HgAuF7fcDnfJLToY7",
    "comentario": "De esos sitios que guardas en favoritos",
    "calidad": 9.4
  },
  {
    "nombre": "Casa Marcos",
    "tipo": "Local",
    "link": "https://maps.app.goo.gl/G7JwvVvvhD4nEgUq8",
    "comentario": "Buen ambiente y mejor comida",
    "calidad": 9.4
  },
  {
    "nombre": "Mahoh",
    "tipo": "Local",
    "link": "https://maps.app.goo.gl/EWxpWRNXjpZp9mr49",
    "comentario": "Plan fácil que siempre funciona",
    "calidad": 9.5
  },
  {
    "nombre": "Cafe Mirante",
    "tipo": "Cafe, desayunos",
    "link": "https://maps.app.goo.gl/y4fWhU3sN2J7dVdP9",
    "comentario": "Aquí no se falla",
    "calidad": 9.2
  },
  {
    "nombre": "Everest",
    "tipo": "Indio",
    "link": "https://maps.app.goo.gl/5TvZq3EiDWbztP7s6",
    "comentario": "Te sientes como en casa",
    "calidad": 8.9
  },
  {
    "nombre": "Lord Nelson",
    "tipo": "Desayunos, live music",
    "link": "https://maps.app.goo.gl/Q45s6W78NS8QNF1T6",
    "comentario": "Un sitio con alma",
    "calidad": 9.1
  },
  {
    "nombre": "La Frasquita",
    "tipo": "Pescado fresco",
    "link": "https://maps.app.goo.gl/Pu9SGqxNh57NFVM47",
    "comentario": "De esos que descubres por casualidad y no olvidas",
    "calidad": 9.3
  },
  {
    "nombre": "Fado Rock",
    "tipo": "Mediterraneo",
    "link": "https://maps.app.goo.gl/D7TsFNuzjGcNgUfN7",
    "comentario": "Perfecto para repetir mil veces",
    "calidad": 9.0
  },
  {
    "nombre": "Caretta Beach La Pared",
    "tipo": "Pescado Fresco",
    "link": "https://maps.app.goo.gl/vsrDCXKb24kesrFZ8",
    "comentario": "De esos sitios que repites sin pensarlo",
    "calidad": 9.4
  },
  {
    "nombre": "La Falua",
    "tipo": "Local",
    "link": "https://maps.app.goo.gl/yJCSmoTUan7gYZQq5",
    "comentario": "Ideal para una comida sin líos",
    "calidad": 9.0
  },
  {
    "nombre": "Mirador de Sotavento",
    "tipo": "Mediterraneo",
    "link": "https://maps.app.goo.gl/pVc65G1F3hFMzZcR6",
    "comentario": "Un clásico que nunca falla",
    "calidad": 9.4
  },
  {
    "nombre": "Marabu",
    "tipo": "Mediterraneo",
    "link": "https://maps.app.goo.gl/4JS192Sk1jx8Qv1c9",
    "comentario": "Un sitio con alma",
    "calidad": 9.2
  }
];