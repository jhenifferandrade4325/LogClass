# importando módulos e classes necessários para a aplicação
from flask import Flask, render_template, request, redirect, session
from conexao import Conexao
from aluno import Aluno
from professor import Professor
from cadastramento import Cadastramento
from estoque import Estoque
from expedicao import Expedicao
from picking import Picking
from pop import Pop
from rnc import Rnc

#app é o servidor
#criei o objeto app usando a classe Flask
app = Flask(__name__)
app.secret_key = 'logclass'

#roteamento da página inicial
@app.route("/")
#função da página inicial
def pagina_inicial():
    if "usuario_logado" in session:
        return render_template("pagina-inicial.html")
    else:
        return redirect("/login")
    
# roteamento da página de cadastro e login que no caso são "juntas" 
# RF001
# RF002
# RF003
# RF004
@app.route("/login", methods=["GET", "POST"])
def pagina_cadastro():
# cada rota processa solicitações GET e POST de forma apropriada, interage com diferentes classes
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        # extraindo os dados que serão recolhidos no formulário
        formulario = request.form.get("tipo")
        # verificando qual o formulário que será usado
        if formulario == "Aluno":
           nome = request.form.get("nome")
           email = request.form.get("email")
           senha = request.form.get("senha")
           turma = request.form.get("turma")
           # criando uma instância da classe aluno
           aluno = Aluno()

            # mandando os dados que foram obtidos para a função que está dentro da classe Aluno
           if aluno.cadastrar(nome, email, senha, turma):
               
               return redirect("/login")
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
            turma = request.form.get("turma")

            loginAluno = Aluno()

            if loginAluno.logar(email, senha, turma):
                # armazena informações do usuário na sessão (session), que é um armazenamento temporário de dados durante a navegação do usuário
                session['usuario_logado'] = {'email':loginAluno.email,
                                            'turma':loginAluno.turma,
                                            'nome':loginAluno.nome,
                                            'cod_aluno':loginAluno.cod_aluno}
                return redirect('/')
            else:
                session.clear()
                return 'Email ou senha incorretos.'
            
        if formulario == "LoginProfessor":
            email = request.form.get("email")
            senha = request.form.get("senha")

            loginProfessor = Professor()

            if loginProfessor.logarProf(email, senha):
                # armazena informações do usuário na sessão (session), que é um armazenamento temporário de dados durante a navegação do usuário
                session['professor_logado'] = {'email':loginProfessor.email_prof,
                                            'nome':loginProfessor.nome_prof,
                                            'senha': loginProfessor.senha_espec}
                return redirect('/')
            else:
                session.clear()
                return 'Email ou senha incorretos.'

# roteamento da página de cadastramento
# RF005
@app.route("/cadastramento", methods=["GET", "POST"])
def pagina_cadastramento():

# as páginas são protegidas por autenticação de sessão para garantir que apenas usuários autenticados possam acessá-las.
    if "usuario_logado" in session:
        if request.method == "GET":
            return render_template("cadastramento.html")
        if request.method == "POST":
            descricao = request.form.get("descricao")
            modelo = request.form.get("modelo")
            fabricante = request.form.get("fabricante")
            codigo = request.form.get("codigo")
            numeroLote = request.form.get("numeroLote")
            enderecamento = request.form.get("enderecamento")
            
            tbCadastramento = Cadastramento()

            if tbCadastramento.cadastramento(codigo, descricao, modelo, fabricante, numeroLote, enderecamento, session['usuario_logado']['turma']):
                return redirect("/")
            else:
                return 'Erro ao realizar o processo de Cadastramento'
    else:
        return redirect("/login")

# roteamento da página dos processos de registro estoque
# RF008
@app.route("/estoque",  methods=["GET", "POST"])
def pagina_estoque():
    if "usuario_logado" in session:
        if request.method == "GET":
            return render_template("estoque.html")
        if request.method == "POST":
            cod_prod = request.form.get("cod_prod")
            num_lote = request.form.get("num_lt")
            loc_ = request.form.get("loc_")
            descricao = request.form.get("descricao")
            dt_enter = request.form.get("dt_enter")
            qt_item = request.form.get("qt_item")
            dt_end = request.form.get("dt_end")
            qt_saida = request.form.get("qt_saida")
            _saldo = request.form.get("_saldo")
            funcionario = request.form.get("funcionario")

            tbEstoque = Estoque()

            if tbEstoque.estoque(cod_prod, num_lote, loc_, descricao, dt_enter, qt_item, dt_end, qt_saida, _saldo, funcionario, session['usuario_logado']['cod_aluno'] , session['usuario_logado']['turma']):
                return redirect("/")
            else:
                return "Erro ao realizar o processo de Controle de Estoque"
    else:
        return redirect("/login")  

# roteamento da página dos processos de registro expedição
# RF010
@app.route("/expedicao", methods=["GET", "POST"])
def pagina_expedicao():
    if "usuario_logado" in session:
        if request.method == "GET":
            return render_template("expedicao.html")
        if request.method == "POST":
            cod_prod = request.form.get("cod_prod")
            data_saida = request.form.get("data_saida")
            num_lote = request.form.get("num_lote")
            responsavel = request.form.get("responsavel")
            quantidade = request.form.get("quantidade")
            descricao_tec = request.form.get("descricao_tec")
            tbExpedicao = Expedicao()
            if tbExpedicao.expedicao(cod_prod, descricao_tec, num_lote, quantidade, data_saida, responsavel, session['usuario_logado']['cod_aluno'], session['usuario_logado']['turma']):
                return redirect ('/')
            else:
                return "Erro ao realizar o processo de cadastro de expedição."
    else:
        return redirect("/login")

# roteamento da página dos processos de registro picking
# RF007
@app.route("/picking", methods=["GET", "POST"])
def pagina_picking():
    if "usuario_logado" in session:
        if request.method == "GET":
            return render_template("picking.html")
        if request.method == "POST":
            numPicking = request.form.get("numPicking")
            enderecamento = request.form.get("enderecamento")
            descTec = request.form.get("descTec")
            modeloPick = request.form.get("modeloPick")
            fabri = request.form.get("fabri")
            qtde = request.form.get("qtde")
            data = request.form.get("data")
            lote = request.form.get("lote")
            totalProd = request.form.get("totalProd")
            codProd = request.form.get("codProd")

            tbpicking = Picking()

            if tbpicking.picking(numPicking, enderecamento, descTec, modeloPick, fabri, qtde, data, lote, totalProd, codProd, session['usuario_logado']['turma']):
                return redirect("/")
            else:
                return 'Erro ao realizar o processo de Picking'
    else:
        return redirect("/login")
    
# roteamento da página dos processos de registro pop
# RF009
@app.route("/pop", methods=["GET", "POST"])
def pagina_pop():
    if "usuario_logado" in session:
        if request.method == "GET":
            return render_template("pop.html")
        if request.method == "POST":
            dt_end1 = request.form.get("dt_end1")
            task_name = request.form.get("task_name")
            resp_ = request.form.get("resp_")
            material = request.form.get("material")
            passos = request.form.get("passos")
            manuseio = request.form.get("manuseio")
            resultados = request.form.get("resultados")
            acoes = request.form.get("acoes")
            tbPop = Pop()
            if tbPop.pop(dt_end1, task_name, resp_, material, passos, manuseio, resultados, acoes, session['usuario_logado']['cod_aluno'], session['usuario_logado']['turma']):
                return redirect ('/')
            else:
                return 'Erro ao realizar o processo de POP'
    else:
        return redirect("/login")

# roteamento da página dos processos de registro rnc
# RF006
@app.route("/rnc", methods=["GET", "POST"])
def pagina_rnc():
    if "usuario_logado" in session:
        if request.method == "GET":
            return render_template("rnc.html")
        if request.method == "POST":
            data = request.form.get("date")
            numRNC = request.form.get("numRNC")
            local = request.form.get("local")
            qtdentregue = request.form.get("qtdentregue")
            qtdrepro = request.form.get("qtdrepro")
            descRNC = request.form.get("descRNC")
            respInsp = request.form.get("respInsp")
            codProd = request.form.get("codProd")

            tbrnc = Rnc()

            if tbrnc.rnc(descRNC, data, numRNC, local, qtdentregue, qtdrepro, respInsp, codProd, session['usuario_logado']['cod_aluno'], session['usuario_logado']['turma']):
                return redirect("/")
            else:
                return 'Erro ao realizar o processo de RNC'
    else:
        return redirect("/login")

app.run(debug=True)