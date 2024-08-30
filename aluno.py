from conexao import Conexao

class Aluno:
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.email = None
        self.senha = None

    # criando uma função para cadastrar o aluno
    def cadastrar (self, cpf, nome, email, senha):
        # conectando com o banco de dados
        mydb = Conexao.conectar()

        mycursor = mydb.cursor()

        dados = f"INSERT INTO tb_aluno (cpf, nome, email, senha) VALUES ('{cpf}', '{nome}', '{email}', '{senha}')"

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

        dados = f"SELECT * FROM database_geral.tb_aluno WHERE email = '{email} AND senha = '{senha}"

        # executando
        mycursor.execute(dados)

        resultado = mycursor.fetchone

        # caso não encontre o usuário com os dados que foram passados 
        if not resultado == None:
            self.logado = True
            self.email = resultado[2]
            self.senha = resultado[3]
        else:
            self.logado = False

        mydb.commit()

        mydb.close()