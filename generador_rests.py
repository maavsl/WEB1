import csv
import json
import os
import random

CSV_FILE = "csv/restaurantes.csv"
OUTPUT_FILE = "salida/data.js"

comentarios_random = [
    "El favorito de mi abuela 👵",
    "Aquí siempre aciertas",
    "Si sobra algo… va para casa 😄",
    "Salí más feliz que un niño en una tienda de caramelos 🍬",
    "De esos sitios que repites sin pensarlo",
    "Comer bien y sin complicaciones",
    "Un clásico que nunca falla",
    "Aquí se viene con hambre y se sale feliz",
    "La comida aquí tiene algo especial",
    "Pequeño pero matón 💥",
    "De los que recomiendas sin dudar",
    "Una sorpresa muy agradable",
    "Ideal para una comida sin líos",
    "De esos sitios que guardas en favoritos",
    "Aquí no se falla",
    "Buen ambiente y mejor comida",
    "Te sientes como en casa",
    "Un sitio con alma",
    "Perfecto para repetir mil veces",
    "Comida rica, servicio rápido y sonrisa asegurada",
    "De esos que descubres por casualidad y no olvidas",
    "Aquí todo sabe mejor",
    "Para venir con hambre de verdad",
    "Plan fácil que siempre funciona",
    "De los que te hacen el día mejor"
]

def generar():
    restaurantes = []
    comentarios_disponibles = comentarios_random.copy()
    random.shuffle(comentarios_disponibles)

    with open(CSV_FILE, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)

        for row in reader:
            nombre = row.get("NOMBRE", "").strip()
            tipo = row.get("TIPO", "").strip()
            link = row.get("ZONA", "").strip()
            comentario_csv = row.get("COMENTARIO", "").strip()

            if not nombre:
                continue

            if comentario_csv:
                comentario = comentario_csv
            else:
                if not comentarios_disponibles:
                    comentarios_disponibles = comentarios_random.copy()
                    random.shuffle(comentarios_disponibles)
                comentario = comentarios_disponibles.pop()

            calidad = round(random.uniform(8.9, 9.7), 1)

            restaurantes.append({
                "nombre": nombre,
                "tipo": tipo,
                "link": link,
                "comentario": comentario,
                "calidad": calidad
            })

    os.makedirs("salida", exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("const RESTAURANTES = ")
        f.write(json.dumps(restaurantes, indent=2, ensure_ascii=False))
        f.write(";")

    print(f"Generados {len(restaurantes)} restaurantes")

generar()