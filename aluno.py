from conexao import Conexao
# classe que irá contar todas as funções referente a tudo que diz respeito ao aluno
class Aluno:
# método construtor em Python, ele é utilizado para inicializar um novo objeto de uma classe
    def __init__(self):
        self.nome = None
        self.email = None
        self.senha = None

    # criando uma função para cadastrar o aluno
    def cadastrar (self, nome, email, senha, turma):
        # conectando com o banco de dados
        mydb = Conexao.conectarAluno(turma)

        mycursor = mydb.cursor()

        dados = f"INSERT INTO tb_aluno (nome, email, senha) VALUES ('{nome}', '{email}', '{senha}')"

        #executar
        mycursor.execute(dados)

        mydb.commit()

        mydb.close()

        return True
    
    # função para logar o aluno 
    def logar (self, email, senha):
        # conectando com o banco de dados
        mydb = Conexao.conectar()

        mycursor = mydb.cursor()

        # variável que armazena uma função do sql
        dados = f"SELECT * FROM database_geral.tb_aluno WHERE email = '{email} AND senha = '{senha}"

        # executando
        mycursor.execute(dados)

        # selecionando apenas um dado do comando acima
        resultado = mycursor.fetchone

        # caso não encontre o usuário com os dados que foram passados 
        if not resultado == None:
            self.logado = True
            self.email = resultado[2]
            self.senha = resultado[3]
            self.nome = resultado[1]
        else:
            self.logado = False

        # salvando os dados 
        mydb.commit()

        # fechando o banco de dados 
        mydb.close()