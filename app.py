from flask import Flask, render_template, request, redirect, session, jsonify

#app é o servidor
#criei o objeto app usando a classe Flask
app = Flask(__name__)
app.secret_key = 'logclass'

#roteamento da página inicial
@app.route("/")
#função da página inicial
def pagina_inicial():
    return render_template("pagina-inicial.html")

# # roteamento da página de cadastro e login que no caso são a mesma
# @app.route("/login")
# def pagina_cadastro():
#     return render_template("login.html")

# roteamento da página de cadastramento
@app.route("/cadastramento")
def pagina_cadastramento():
     return render_template("cadastramento.html")

# # roteamento da página dos processos de registro estoque
# @app.route("/estoque")
# def pagina_estoque():
#     return render_template("estoque.html")

# # roteamento da página dos processos de registro expedição
# @app.route("/expedicao")
# def pagina_expedicao():
#     return render_template("expedicao.html")

# # roteamento da página dos processos de registro picking
# @app.route("/picking")
# def pagina_picking():
#     return render_template("picking.html")

# # roteamento da página dos processos de registro pop
# @app.route("/pop")
# def pagina_pop():
#     return render_template("pop.html")

# # roteamento da página dos processos de registro rnc
# @app.route("/rnc")
# def pagina_rnc():
#     return render_template("rnc.html")

app.run(debug=True)