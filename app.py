from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo="Bienvenido a la página principal de mi proyecto Flask.")

@app.route('/about')
def about():
    return render_template('about.html', titulo="Esta es la página de “Acerca de” del proyecto Flask")

@app.route('/usuarios/<nombre>')
def usuario(nombre):
    return render_template('base.html', titulo=f"Hola, {nombre}", mensaje=f"Bienvenido {nombre} a la app")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render asigna puerto automáticamente
    app.run(host="0.0.0.0", port=port, debug=True)
