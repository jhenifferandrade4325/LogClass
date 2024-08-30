from conexao import Conexao
class Estoque:
    def __init__(self):
        # inicializa os atributos da classe com o valor None
        self.cod_prod_est = None
        self.num_lote_est = None
        self.loc_est = None
        self.desc_tec = None
        self.data_entrega = None
        self.quant_itens_entrada = None
        self.data_saida = None
        self.quant_saida = None
        self.saldo = None
        self.func_responsavel = None
        self.cpf = None

    # função para o cadastro de estoque
    def estoque (self, cod_prod_est, num_lote_est, loc_est, desc_tec, data_entrega, quant_itens_entrada, data_saida, saldo, fuc_responsavel, cpf):
        # conectando com o banco de dados
        mydb = Conexao.conectar()

        # criando um cursor para executar comandos SQL na conexão com o banco de dados
        mycursor = mydb.cursor()

        dados = f"INSERT INTO tb_estoque(cod_prod_est, num_lote_est, loc_est, desc_tec, data_entrega, quant_itens_entrada, data_saida, saldo, fuc_responsavel, cpf) VALUES ('{cod_prod_est}', '{num_lote_est}', '{loc_est}', '{desc_tec}', '{data_entrega}', '{quant_itens_entrada}', '{data_saida}', '{saldo}', '{fuc_responsavel}', '{cpf}')"

        #executando o comando que foi determinado a cima
        mycursor.execute(dados)

        # realiza o commit da transação, garantindo que as alterações feitas na base de dados sejam salvas
        mydb.commit()

        mydb.close()

        # retorna True indicando que a operação foi realizada com sucesso
        return True