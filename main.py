import requests

# API pública (ejemplo: chistes aleatorios)
url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)
data = response.json()

# Crear HTML con el resultado
html = f"""
<html>
<head><title>Demo GitHub Actions</title></head>
<body>
  <h1>Chiste aleatorio desde API 😄</h1>
  <p><b>{data['setup']}</b></p>
  <p>{data['punchline']}</p>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Archivo HTML generado con éxito ✅")
