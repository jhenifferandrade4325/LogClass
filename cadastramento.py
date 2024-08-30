from conexao import Conexao
class Cadastramento:
    def __init__(self):
        # inicializa os atributos da classe com o valor None
        self.cod_prod = None
        self.descricao_tecnica = None
        self.modelo = None
        self.fabricante = None
        self.num_lote = None
        self.enderecamento = None
        self.cpf_prof = None

    # função para cadastrar os produtos
    def cadastramento (self, cod_prod, descricao_tecnica, modelo, fabricante, num_lote, enderecamento, cpf_prof):
        # conectando com o banco de dados
        mydb = Conexao.conectar()

        # criando um cursor para executar comandos SQL na conexão com o banco de dados
        mycursor = mydb.cursor()

        dados = f"INSERT INTO tb_cadastramento (cod_prod, descricao_tecnica, modelo, fabricante, num_lote, enderecamento, cpf_prof) VALUES ('{cod_prod}', '{descricao_tecnica}', '{modelo}', '{fabricante}', '{num_lote}', '{enderecamento}', '{cpf_prof}')"

        #executando a variável a cima
        mycursor.execute(dados)

        # realiza o commit da transação, garantindo que as alterações feitas na base de dados sejam salvas
        mydb.commit()

        mydb.close()

        return True