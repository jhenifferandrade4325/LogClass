from conexao import Conexao

class Rnc:
    def __init__(self):
        self.desc_rnc = None
        self.recebimento = None
        self.num_rnc = None
        self.local_rnc = None
        self.quant_entregue = None
        self.quant_reprovada = None
        self.resp_inspecao = None
        self.cpf = None
        self.cod_prod = None

    # criando uma função para que seja possível a realização do processo de rnc
    def rnc(self, desc_rnc, recebimento, num_rnc, local_rnc, quant_entregue, quant_reprovada, resp_inspecao, cpf, cod_prod):
        # conectando com o banco de dados
        mydb = Conexao.conectar()

        mycursor = mydb.cursor()

        dados = f"INSERT INTO tb_rnc(desc_rnc, recebimento, num_rnc, local_rnc, quant_entregue, quant_reprovada, resp_inspecao, cpf, cod_prod) VALUES('{desc_rnc}', '{recebimento}', '{num_rnc}', '{local_rnc}', '{quant_entregue}', '{quant_reprovada}', '{resp_inspecao}', '{cpf}', '{cod_prod}')"

        #executar
        mycursor.execute(dados)

        # realiza o commit da transação, garantindo que as alterações feitas na base de dados sejam salvas
        mydb.commit()

        mydb.close()
        
        # retorna True indicando que a operação foi realizada com sucesso
        return True