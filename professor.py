from conexao import Conexao

class Professor:
    def __init__(self):
        self.nome_prof = None
        self.email_prof = None
        self.senha_espec = None

    # criando função para cadastrar o professor
    def cadastrarProf (self, nome_prof, email_prof, senha_espec):
        # conectando com o banco de dados
        mydb = Conexao.conectar()

        mycursor = mydb.cursor()

        dados = f"INSERT INTO tb_professor (nome_prof, email_prof, senha_espec) VALUES ('{nome_prof}', '{email_prof}', '{senha_espec}')"

        #executar
        mycursor.execute(dados)

        mydb.commit()

        mydb.close()

        return True

    # logando o professor
    def logarProf (self, email_prof, senha_espec):
        # conectando com o banco de dados
        mydb = Conexao.conectar()

        mycursor = mydb.cursor()

        dados = f"SELECT * FROM database_geral.tb_professor WHERE email_prof = '{email_prof} AND senha_espec = '{senha_espec}"

        # executando
        mycursor.execute(dados)

        resultado = mycursor.fetchone

        # caso não encontre o usuário com os dados que foram passados 
        if not resultado == None:
            self.logado = True
            self.email_prof = resultado[2]
            self.senha_espec = resultado[3]
        else:
            self.logado = False

        mydb.commit()

        mydb.close()