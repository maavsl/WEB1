import csv
import os

PLANTILLA = "plantilla.html"
CARPETA_CSV = "csv"
SALIDA = "salida"

def leer_csv(ruta):
    datos = {}

    with open(ruta, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)

        for fila in reader:
            fila = [c.strip() for c in fila]

            if len(fila) >= 2 and fila[0] and fila[1]:
                datos[fila[0]] = fila[1]

            if len(fila) >= 3 and not fila[0] and fila[1] and fila[2]:
                datos[fila[1]] = fila[2]

    return datos

def buscar(datos, posibles_claves):
    claves_norm = {k.lower().strip(): v for k, v in datos.items()}

    for clave in posibles_claves:
        clave_norm = clave.lower().strip()
        for k, v in claves_norm.items():
            if clave_norm in k and v.strip():
                return v.strip()

    return "N/A"

def generar_html(datos, plantilla):
    reemplazos = {
        "Nombre de la vivienda": buscar(datos, ["Nombre de la vivienda"]),
        "Dirección": buscar(datos, ["Dirección"]),
        "Link maps": buscar(datos, ["Link maps"]),
        "Link video": buscar(datos, ["Link video", "Video", "Vídeo", "Link Video"]),
        "Codigo Caja": buscar(datos, ["Codigo Caja", "Código Caja"]),
        "telefono": buscar(datos, ["telefono", "Teléfono"]),
        "Fotos": buscar(datos, ["Fotos"]),
        "Link Normas": buscar(datos, ["Link Normas"]),
        "Basura": buscar(datos, ["Basura"]),
        "Supermercados": buscar(datos, ["Supermercados"]),
        "Playas y Actividades": buscar(datos, ["Playas y Actividades"]),
        "Restaurantes": buscar(datos, ["Restaurantes"]),
        "Fuerte en 7 dias": buscar(datos, ["Fuerte en 7 dias", "Fuerte en 7 días"]),
        "Piscina": buscar(datos, ["Piscina"]),
        "Parking": buscar(datos, ["Parking"]),
        "Taxi": buscar(datos, ["Taxi", "Taxi aproximado", "Taxi (aproximado)"]),
        "Te podemos llevar": buscar(datos, ["Te podemos llevar", "Te podemos llevar max 2 personas", "Te podemos llevar (max 2 personas)"]),
        "Bus": buscar(datos, ["Bus"])
    }

    html = plantilla

    for campo, valor in reemplazos.items():
        html = html.replace("{{" + campo + "}}", valor)

    return html

def nombre_salida(archivo):
    nombre = archivo.replace(".csv", "")
    if " - " in nombre:
        nombre = nombre.split(" - ")[-1]
    return nombre.strip().lower().replace(" ", "_") + ".html"

def titulo_desde_archivo(archivo):
    return archivo.replace(".html", "").replace("_", " ").title()

def generar_index():
    archivos = [
        f for f in os.listdir(SALIDA)
        if f.lower().endswith(".html")
    ]

    enlaces = ""

    for archivo in sorted(archivos):
        nombre = titulo_desde_archivo(archivo)
        enlaces += f'    <a class="card" href="salida/{archivo}">{nombre}</a>\n'

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MAAV - Viviendas</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      background: #f4f1ea;
      margin: 0;
      padding: 24px;
      color: #1f2933;
    }}
    h1 {{
      font-size: 32px;
      margin-bottom: 8px;
    }}
    p {{
      font-size: 16px;
      color: #667085;
      margin-bottom: 24px;
    }}
    .grid {{
      display: grid;
      gap: 14px;
      max-width: 720px;
    }}
    .card {{
      display: block;
      background: white;
      padding: 20px;
      border-radius: 18px;
      text-decoration: none;
      color: #1f2933;
      font-size: 22px;
      font-weight: 700;
      box-shadow: 0 6px 18px rgba(0,0,0,.08);
    }}
  </style>
</head>
<body>
  <h1>Viviendas MAAV</h1>
  <p>Listado automático de páginas disponibles.</p>
  <div class="grid">
{enlaces}  </div>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Index generado")

def main():
    os.makedirs(SALIDA, exist_ok=True)

    with open(PLANTILLA, encoding="utf-8") as f:
        plantilla = f.read()

    for archivo in os.listdir(CARPETA_CSV):
        if archivo.lower().endswith(".csv"):
            ruta = os.path.join(CARPETA_CSV, archivo)
            datos = leer_csv(ruta)
            html = generar_html(datos, plantilla)

            nombre = nombre_salida(archivo)
            salida = os.path.join(SALIDA, nombre)

            with open(salida, "w", encoding="utf-8") as f:
                f.write(html)

            print("Generado:", nombre)

    generar_index()

main()