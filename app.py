from flask import Flask, render_template, request, redirect, session, jsonify


#app é o servidor
#criei o objeto app usando a classe Flask
app = Flask(__name__)
app.secret_key = 'logclass'

#roteamento da página
@app.route("/")
#função da página inicial
def pagina_inicial():
    return render_template("pagina-inicial.html")

app.run(debug=True)