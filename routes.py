## IMPORTS
from flask import Flask, render_template,url_for

# Criar app
app = Flask(__name__)

## ROTAS 
@app.route('/')
def loginpage():
    return render_template("login.html")

@app.route('/registrar')
def registrar():
    return render_template('registrar.html')