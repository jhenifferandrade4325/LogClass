from conexao import Conexao
# classe que irá armazenar as funções referentes ao processo de cadastro de expedição
class Expedicao:
    def __init__(self):
        self.cod_prod_exp = None
        self.desc_exp = None
        self.num_lote_exp = None
        self.quant_exp = None
        self.data_emb_exp = None
        self.responsavel_exp = None
        self.cpf = None
        self.cod_prod = None

    # criando a função para cadastro da expedição dos produtos
    def estoque(self, cod_prod_exp, desc_exp, num_lote_exp, quant_exp, data_emb_exp, responsavel_exp, cpf, cod_prod):
        # conectando com o banco de dados
        mydb = Conexao.conectar()

        mycursor = mydb.cursor()

        dados = f"INSERT INTO tb_estoque(cod_prod_exp, desc_exp, num_lote_exp, quant_exp, data_emb_exp, responsavel_exp, cpf, cod_prod) VALUES ('{cod_prod_exp}', '{desc_exp}', '{num_lote_exp}', '{quant_exp}', '{data_emb_exp}', '{responsavel_exp}', '{cpf}', '{cod_prod}')"

        #executar
        mycursor.execute(dados)

        mydb.commit()

        mydb.close()

        return True