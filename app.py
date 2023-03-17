from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "<h1>Hello World with Github Actions/GCP</h1><br><br><b>#fiap #10aso</b>"