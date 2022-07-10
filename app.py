from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "<h1>Hello World with Github Actions/Heroku</h1><br><br><b>#fiap #10aso</b>"

if __name__ == '__main__':
    app.run()