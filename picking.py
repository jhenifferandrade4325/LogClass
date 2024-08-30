from conexao import Conexao

class Picking:
    def __init__(self):
        self.cod_produto = None
        self.endereco = None
        self.desc_tecnica = None
        self.modelo_pk = None
        self.fabricante_pk = None
        self.quant_pk = None
        self.data_pk = None
        self.lote_pk = None
        self.num_picking = None
        self.total_pk = None
        self.cod_prod = None

    # criando a função para que possa ser realizado o processo de picking
    def picking(self, cod_produto, endereco, desc_tecnica, modelo_pk, fabricante_pk, quant_pk, data_pk, lote_pk, num_picking, total_pk, cod_prod):
        # conectando com o banco de dados
        mydb = Conexao.conectar()

        mycursor = mydb.cursor()

        dados = f"INSERT INTO tb_picking(cod_produto, endereco, desc_tecnica, modelo_pk, fabricante_pk, quant_pk, data_pk, lote_pk, num_picking, total_pk, cod_prod) VALUES('{cod_produto}', '{endereco}', '{desc_tecnica}', '{modelo_pk}', '{fabricante_pk}', '{quant_pk}', '{data_pk}', '{lote_pk}', '{num_picking}', '{total_pk}', '{cod_prod}')"

        #executar
        mycursor.execute(dados)

        mydb.commit()

        mydb.close()

        return True