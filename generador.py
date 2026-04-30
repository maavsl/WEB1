def generar_index():
    archivos = []

    # HTML antiguos en la raíz
    for f in os.listdir("."):
        if f.lower().endswith(".html") and f != "index.html" and f != "plantilla.html":
            archivos.append((f, f))

    # HTML nuevos dentro de salida
    for f in os.listdir(SALIDA):
        if f.lower().endswith(".html"):
            archivos.append((os.path.join("salida", f), f))

    enlaces = ""

    for ruta, archivo in sorted(archivos, key=lambda x: x[1].lower()):
        nombre = titulo_desde_archivo(archivo)
        enlaces += f'    <a class="card" href="{ruta}">{nombre}</a>\n'

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