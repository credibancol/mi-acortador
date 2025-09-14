from flask import Flask, render_template, request, redirect, url_for
import string, random

app = Flask(__name__)

# Generar un string corto aleatorio
def generar_codigo():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

urls = {}

@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None
    if request.method == "POST":
        url_original = request.form["url"]
        codigo = generar_codigo()
        urls[codigo] = url_original
        short_url = request.host_url + codigo
    return render_template("index.html", short_url=short_url)

@app.route("/<codigo>")
def redirigir(codigo):
    url = urls.get(codigo)
    if url:
        return redirect(url)
    return "URL no encontrada", 404

if __name__ == "__main__":
    app.run(debug=True)
