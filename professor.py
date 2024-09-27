from conexao import Conexao
# classe que armazena as funções referentes ao processo de cadastro e login do professor
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

        dados = f"INSERT INTO tb_aluno (nome, email, senha) VALUES ('{nome_prof}', '{email_prof}', '{senha_espec}')"

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

        dados = f"SELECT * FROM tb_aluno WHERE email = '{email_prof}' AND senha = '{senha_espec}'"

        # executando
        mycursor.execute(dados)

        resultado = mycursor.fetchone()

        mydb.close()

        # caso não encontre o usuário com os dados que foram passados 
        if not resultado == None:
            self.logado = True
            self.email_prof = resultado[2]
            self.senha_espec = resultado[3]
            return True
        else:
            self.logado = False
            return False



    def criaDatabse(self, bancodedados):
        # conectando com o banco de dados
        mydb = Conexao.conectar()

        mycursor = mydb.cursor()

        # variável que armazena o comando que executará um novo banco de dados
        # criando um banco de dados caso ele ainda não exista (IF NOT EXISTS)
        dados = [
            f"""
                CREATE DATABASE IF NOT EXISTS {bancodedados};
            """,
            f"""
                USE {bancodedados};
            """,
            """
                CREATE TABLE tb_aluno (
                cod_aluno INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                senha VARCHAR(100) NOT NULL
                );
            """,
            """
                CREATE TABLE tb_cadastramento (
                cod_prod VARCHAR(100) NOT NULL,
                descricao_tecnica VARCHAR(100) NOT NULL,
                modelo VARCHAR(100) NOT NULL,
                fabricante VARCHAR(100) NOT NULL,
                num_lote VARCHAR(100) NOT NULL,
                enderecamento VARCHAR(100) NOT NULL
                );
            """,
            """
                ALTER TABLE tb_cadastramento ADD CONSTRAINT PK_tb_cadastramento PRIMARY KEY (cod_prod);
            """,
            """
                CREATE TABLE tb_estoque (
                cod_prod_est INT NOT NULL,
                num_lote_est INT NOT NULL,
                loc_est CHAR(100) NOT NULL,
                desc_tec VARCHAR(100) NOT NULL,
                data_entrega DATE NOT NULL,
                quant_itens_entrada INT NOT NULL,
                data_saida DATE NOT NULL,
                quant_saida INT NOT NULL,
                saldo INT NOT NULL,
                func_responsavel VARCHAR(100) NOT NULL,
                cod_aluno INT
                );
            """,
            """
                ALTER TABLE tb_estoque ADD CONSTRAINT PK_tb_estoque PRIMARY KEY (cod_prod_est);
            """,
            """
                CREATE TABLE tb_expedicao (
                cod_prod_exp VARCHAR(100) NOT NULL,
                desc_exp VARCHAR(100) NOT NULL,
                num_lote_exp VARCHAR(100) NOT NULL,
                quant_exp VARCHAR(100) NOT NULL,
                data_emb_exp DATE NOT NULL,
                respnsavel_exp VARCHAR(100) NOT NULL,
                cod_aluno INT 
                );
            """,
            """
                ALTER TABLE tb_expedicao ADD CONSTRAINT PK_tb_expedicao PRIMARY KEY (cod_prod_exp);
            """,
            """
                CREATE TABLE tb_picking (
                num_picking INT NOT NULL,
                endereco VARCHAR(100) NOT NULL,
                desc_tecnica VARCHAR(100) NOT NULL,
                modelo_pk VARCHAR(100) NOT NULL,
                fabricante_pk VARCHAR(100) NOT NULL,
                quant_pk INT NOT NULL,
                data_pk DATE NOT NULL,
                lote_pk VARCHAR(100) NOT NULL,
                total_pk INT NOT NULL,
                cod_prod VARCHAR(100) 
                );
            """,
            """
                ALTER TABLE tb_picking ADD CONSTRAINT PK_tb_picking PRIMARY KEY (num_picking);
            """,
            """
                CREATE TABLE tb_pop (
                cod_pop INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                data_pop DATE NOT NULL,
                tarefa_pop VARCHAR(100) NOT NULL,
                responsavel_pop VARCHAR(100) NOT NULL,
                material_pop VARCHAR(100) NOT NULL,
                passos_pop VARCHAR(100) NOT NULL,
                manuseio_pop VARCHAR(100) NOT NULL,
                resul_pop VARCHAR(100) NOT NULL,
                acao_pop VARCHAR(100) NOT NULL,
                cod_aluno INT 
                );
            """,
            """
                CREATE TABLE tb_rnc (
                desc_rnc VARCHAR(100) NOT NULL,
                recebimento DATE NOT NULL,
                num_rnc VARCHAR(100) NOT NULL,
                local_rnc VARCHAR(100) NOT NULL,
                quant_entregue INT NOT NULL,
                quant_reprovada INT NOT NULL,
                resp_inspecao VARCHAR(100) NOT NULL,
                cod_prod VARCHAR(100) NOT NULL,
                cod_aluno INT 
                );
            """,
            """
                ALTER TABLE tb_rnc ADD CONSTRAINT PK_tb_rnc PRIMARY KEY (desc_rnc);
            """,
            """
                ALTER TABLE tb_estoque ADD CONSTRAINT FK_tb_estoque_0 FOREIGN KEY (cod_aluno) REFERENCES tb_aluno (cod_aluno);
            """,
            """
                ALTER TABLE tb_expedicao ADD CONSTRAINT FK_tb_expedicao_0 FOREIGN KEY (cod_prod_exp) REFERENCES tb_cadastramento (cod_prod);
            """,
            """
                ALTER TABLE tb_expedicao ADD CONSTRAINT FK_tb_expedicao_1 FOREIGN KEY (cod_aluno) REFERENCES tb_aluno (cod_aluno);
            """,
            """
                ALTER TABLE tb_picking ADD CONSTRAINT FK_tb_picking_0 FOREIGN KEY (cod_prod) REFERENCES tb_cadastramento (cod_prod);
            """,
            """
                ALTER TABLE tb_pop ADD CONSTRAINT FK_tb_pop_0 FOREIGN KEY (cod_aluno) REFERENCES tb_aluno (cod_aluno);
            """,
            """
                ALTER TABLE tb_rnc ADD CONSTRAINT FK_tb_rnc_0 FOREIGN KEY (cod_prod) REFERENCES tb_cadastramento (cod_prod);
            """,
            """
                ALTER TABLE tb_rnc ADD CONSTRAINT FK_tb_rnc_1 FOREIGN KEY (cod_aluno) REFERENCES tb_aluno (cod_aluno);
            """
        ]
            

        #executar
        # Executar cada comando de criação de tabela
        for comando in dados:
            print(comando)
            mycursor.execute(comando)

        # salvar o que foi adicionado ao banco de dados
        mydb.commit()
        
        nomes = f"INSERT into databaseprofessor.tb_database (nomeBase) VALUES ('{bancodedados}')"
        mycursor.execute(nomes)
        mydb.commit()
        
        # fechando o banco de dados
        mydb.close()

        # retornando um valor verdadeiro
        return True