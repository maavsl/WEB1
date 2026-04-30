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
    nombre = archivo.replace(".html", "").replace("_", " ").title()
    nombre = nombre.replace("P23", "P23").replace("P89", "P89")
    nombre = nombre.replace("Pm", "PM").replace("Vm", "VM")
    return nombre

def generar_index():
    especiales = [
        ("🍽️ Restaurantes", "restaurantes.html"),
        ("📋 Reglas", "reglas.html"),
        ("🗺️ 7 días en Fuerteventura", "7dias.html"),
    ]

    archivos = [
        f for f in os.listdir(SALIDA)
        if f.lower().endswith(".html")
    ]

    viviendas = []

    for archivo in sorted(archivos):
        if archivo.lower() in ["restaurantes.html", "index.html"]:
            continue

        nombre = titulo_desde_archivo(archivo)
        viviendas.append((nombre, f"salida/{archivo}"))

    especiales_html = ""
    for nombre, ruta in especiales:
        if os.path.exists(ruta):
            especiales_html += f'    <a class="card especial" href="{ruta}">{nombre}</a>\n'

    viviendas_html = ""
    for nombre, ruta in viviendas:
        viviendas_html += f'    <a class="card vivienda" href="{ruta}">{nombre}</a>\n'

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MAAV</title>
<style>
body {{
  font-family: Arial, sans-serif;
  background: #f4f1ea;
  margin: 0;
  padding: 24px;
  color: #1f2933;
}}

h1 {{
  font-size: 34px;
  margin: 0 0 8px;
}}

.sub {{
  color: #667085;
  font-size: 16px;
  margin: 0 0 24px;
}}

.section {{
  margin: 30px 0 12px;
  font-size: 17px;
  font-weight: 900;
  color: #667085;
  text-transform: uppercase;
  letter-spacing: .08em;
}}

.grid {{
  display: grid;
  gap: 14px;
  max-width: 760px;
}}

.card {{
  display: block;
  padding: 22px;
  border-radius: 18px;
  text-decoration: none;
  font-size: 22px;
  font-weight: 850;
  box-shadow: 0 8px 22px rgba(0,0,0,.08);
}}

.especial {{
  background: #ffffff;
  color: #1f2933;
}}

.vivienda {{
  background: #0f766e;
  color: white;
}}

.card:active {{
  transform: scale(.99);
}}

@media (max-width: 600px) {{
  body {{
    padding: 18px;
  }}

  h1 {{
    font-size: 30px;
  }}

  .card {{
    font-size: 21px;
    padding: 22px;
  }}
}}
</style>
</head>
<body>

<h1>MAAV</h1>
<p class="sub">Guías rápidas para huéspedes.</p>

<div class="section">General</div>
<div class="grid">
{especiales_html}</div>

<div class="section">Viviendas</div>
<div class="grid">
{viviendas_html}</div>

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