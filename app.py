from flask import Flask, render_template, request, redirect, session, jsonify
from conexao import Conexao
from aluno import Aluno
from professor import Professor

#app é o servidor
#criei o objeto app usando a classe Flask
app = Flask(__name__)
app.secret_key = 'logclass'

#roteamento da página inicial
@app.route("/")
#função da página inicial
def pagina_inicial():
    return render_template("pagina-inicial.html")

# roteamento da página de cadastro e login que no caso são a mesma
@app.route("/login", methods=["GET", "POST"])
def pagina_cadastro():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        # extraindo os dados que serão recolhidos no formulário
        formulario = request.form.get("tipo")
        if formulario == "Aluno":
           nome = request.form.get("nome")
           email = request.form.get("email")
           senha = request.form.get("senha")
           turma = request.form.get("turma")
           # criando uma instância da classe aluno
           aluno = Aluno()

           if aluno.cadastrar(nome, email, senha, turma):
               return redirect("/")
           else:
               return "Erro ao Cadastrar o aluno"
           
        if formulario == "Professor":
            nome = request.form.get("nome")
            email = request.form.get("email")
            senha = request.form.get("senha")
            professor = Professor()

            if senha == "logclass":
                if professor.cadastrarProf(nome, email, senha):
                    return redirect("/")
                else:
                    return "Erro ao Cadastrar o professor"
            else:
                return redirect("/login")

        if formulario == "LoginAluno":
            email = request.form.get("email")
            senha = request.form.get("senha")

            loginAluno = Aluno()

            if loginAluno.logar(email, senha):
                session['usuario_logado'] = {'email':loginAluno.email,
                                            'senha':loginAluno.senha}
                return redirect('/')
            else:
                session.clear()
                return 'Email ou senha incorretos.'

# # roteamento da página de cadastramento
# @app.route("/cadastramento", methods=["GET", "POST"])
# def pagina_cadastramento():
    # if request.method == "GET":
    #     return render_template("cadastramento.html")
    # if request.method == "POST":

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