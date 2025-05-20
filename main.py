## IMPORTS
from flask import Flask, render_template

# Criar app
app = Flask(__name__)

## ROTAS 
@app.route('/')
def homepage():
    return render_template("home.html")

# Iniciar programa
if __name__ == "__main__":
    app.run()