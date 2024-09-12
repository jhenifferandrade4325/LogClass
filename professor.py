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

    def criaDatabse(bancodedados):
        # conectando com o banco de dados
        mydb = Conexao.conectar()

        mycursor = mydb.cursor()

        # variável que armazena o comando que executará um novo banco de dados
        dados = f"
            # criando um banco de dados caso ele ainda não exista (IF NOT EXISTS)
            CREATE DATABASE IF NOT EXISTS database_geral;
            USE database_geral;

            CREATE TABLE IF NOT EXISTS tb_aluno (
                cod_aluno INT NOT NULL AUTO_INCREMENT,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                senha VARCHAR(100) NOT NULL,
                PRIMARY KEY (cod_aluno)
            );

            CREATE TABLE IF NOT EXISTS tb_cadastramento (
                cod_prod VARCHAR(10) NOT NULL,
                descricao_tecnica VARCHAR(100) NOT NULL,
                modelo VARCHAR(50) NOT NULL,
                fabricante VARCHAR(50) NOT NULL,
                num_lote VARCHAR(20) NOT NULL,
                enderecamento VARCHAR(100) NOT NULL,
                PRIMARY KEY (cod_prod)
            );

            CREATE TABLE IF NOT EXISTS tb_estoque (
                cod_prod_est INT NOT NULL AUTO_INCREMENT,
                num_lote_est VARCHAR(20) NOT NULL,
                loc_est CHAR(10) NOT NULL,
                desc_tec VARCHAR(100) NOT NULL,
                data_entrega DATE NOT NULL,
                quant_itens_entrada INT NOT NULL,
                data_saida DATE NOT NULL,
                quant_saida INT NOT NULL,
                saldo INT NOT NULL,
                func_responsavel VARCHAR(100) NOT NULL,
                cod_aluno INT NOT NULL,
                PRIMARY KEY (cod_prod_est),
                FOREIGN KEY (cod_aluno) REFERENCES tb_aluno(cod_aluno)
            );

            CREATE TABLE IF NOT EXISTS tb_expedicao (
                cod_prod_exp VARCHAR(10) NOT NULL,
                desc_exp VARCHAR(100) NOT NULL,
                num_lote_exp VARCHAR(20) NOT NULL,
                quant_exp INT NOT NULL,
                data_emb_exp DATE NOT NULL,
                responsavel_exp VARCHAR(100) NOT NULL,
                cod_prod VARCHAR(10) NOT NULL,
                cod_aluno INT NOT NULL,
                PRIMARY KEY (cod_prod_exp),
                FOREIGN KEY (cod_prod) REFERENCES tb_cadastramento(cod_prod),
                FOREIGN KEY (cod_aluno) REFERENCES tb_aluno(cod_aluno)
            );

            CREATE TABLE IF NOT EXISTS tb_picking (
                cod_produto VARCHAR(10) NOT NULL,
                endereco VARCHAR(100) NOT NULL,
                desc_tecnica VARCHAR(100) NOT NULL,
                modelo_pk VARCHAR(50) NOT NULL,
                fabricante_pk VARCHAR(50) NOT NULL,
                quant_pk INT NOT NULL,
                data_pk DATE NOT NULL,
                lote_pk VARCHAR(20) NOT NULL,
                num_picking INT NOT NULL,
                total_pk INT NOT NULL,
                cod_prod VARCHAR(10) NOT NULL,
                PRIMARY KEY (cod_produto),
                FOREIGN KEY (cod_prod) REFERENCES tb_cadastramento(cod_prod)
            );

            CREATE TABLE IF NOT EXISTS tb_pop (
                cod_pop CHAR(10) NOT NULL,
                data_pop DATE NOT NULL,
                tarefa_pop VARCHAR(100) NOT NULL,
                responsavel_pop VARCHAR(100) NOT NULL,
                material_pop VARCHAR(100) NOT NULL,
                passos_pop TEXT NOT NULL,
                manuseio_pop TEXT NOT NULL,
                resultado_pop TEXT NOT NULL,
                acao_pop TEXT NOT NULL,
                cod_aluno INT NOT NULL,
                PRIMARY KEY (cod_pop),
                FOREIGN KEY (cod_aluno) REFERENCES tb_aluno(cod_aluno)
            );

            CREATE TABLE IF NOT EXISTS tb_rnc (
                desc_rnc VARCHAR(100) NOT NULL,
                recebimento DATE NOT NULL,
                num_rnc VARCHAR(20) NOT NULL,
                local INT NOT NULL,
                quant_entregue INT NOT NULL,
                quant_reprovada INT NOT NULL,
                resp_inspecao VARCHAR(100) NOT NULL,
                cod_prod VARCHAR(10) NOT NULL,
                cod_aluno INT NOT NULL,
                PRIMARY KEY (desc_rnc),
                FOREIGN KEY (cod_prod) REFERENCES tb_cadastramento(cod_prod),
                FOREIGN KEY (cod_aluno) REFERENCES tb_aluno(cod_aluno)
            );
        "

        #executar
        mycursor.execute(dados)

        # salvar o que foi adicionado ao banco de dados
        mydb.commit()

        # fechando o banco de dados
        mydb.close()

        # retornando um valor verdadeiro
        return True