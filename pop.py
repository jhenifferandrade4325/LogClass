from conexao import Conexao

class Pop:
    def __init__(self):
        self.cod_pop = None
        self.data_pop = None
        self.tarefa_pop = None
        self.responsavel_pop = None
        self.material_pop = None
        self.passos_pop = None
        self.manuseio_pop = None
        self.resul_pop = None
        self.acao_pop = None
        self.cpf = None
    
    # criando a função para realizar o processo de pop
    def pop(self, cod_pop, data_pop, tarefa_pop, responsavel_pop, material_pop, passos_pop, manuseio_pop, resul_pop, acao_pop, cpf):
        # conectando com o banco de dados
        mydb = Conexao.conectar()

        mycursor = mydb.cursor()

        dados = f"INSERT INTO tb_pop(cod_pop, data_pop, tarefa_pop, responsavel_pop, material_pop, passos_pop, manuseio_pop, resul_pop, acao_pop, cpf) VALUES('{cod_pop}', '{data_pop}', '{tarefa_pop}', '{responsavel_pop}', '{material_pop}', '{passos_pop}', '{manuseio_pop}', '{resul_pop}', '{acao_pop}', '{cpf}')"

        #executar
        mycursor.execute(dados)

        mydb.commit()

        mydb.close()

        return True