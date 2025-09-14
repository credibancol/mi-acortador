from flask import Flask, request, redirect, render_template_string
import string, random

app = Flask(__name__)
urls = {}

HTML_FORM = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Acortador</title>
</head>
<body>
    <h2>Acortador de URL</h2>
    <form method="post">
        <input type="text" name="url" placeholder="Pega tu enlace aquí" required>
        <button type="submit">Acortar</button>
    </form>
    {% if short_url %}
        <p>Tu enlace acortado: 
            <a href="{{ short_url }}" target="_blank">{{ short_url }}</a>
        </p>
    {% endif %}
</body>
</html>
'''

def generar_codigo():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None
    if request.method == "POST":
        original_url = request.form["url"]
        codigo = generar_codigo()
        urls[codigo] = original_url
        short_url = request.host_url + codigo
    return render_template_string(HTML_FORM, short_url=short_url)

@app.route("/<codigo>")
def redirigir(codigo):
    url = urls.get(codigo)
    if url:
        return redirect(url)
    return "URL no encontrada", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
