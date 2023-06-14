from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return '<h1><br><br><center>SOLUTION SPRINT FASE 5<center></h1><br><br><b><center><img src="https://media.tenor.com/gpgRaDj_ym4AAAAd/acabou-pel%C3%AA.gif" width="172.66" height="97.125"></center><p style="text-align:right">#fiap #10asoo #agoravai</p>'