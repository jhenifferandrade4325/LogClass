CREATE DATABASE database_geral;
USE database_geral;

CREATE TABLE tb_aluno (
 cpf VARCHAR(10) NOT NULL,
 nome VARCHAR(10) NOT NULL,
 email VARCHAR(10) NOT NULL,
 senha VARCHAR(10) NOT NULL
);

ALTER TABLE tb_aluno ADD CONSTRAINT PK_tb_aluno PRIMARY KEY (cpf);


CREATE TABLE tb_estoque (
 cod_prod_est INT NOT NULL,
 num_lote_est INT NOT NULL,
 loc_est CHAR(10) NOT NULL,
 desc_tec VARCHAR(10) NOT NULL,
 data_entrega INT NOT NULL,
 quant_itens_entrada INT NOT NULL,
 data_saida INT NOT NULL,
 quant_saida INT NOT NULL,
 saldo INT NOT NULL,
 func_responsavel VARCHAR(10) NOT NULL,
 cpf VARCHAR(10)
);

ALTER TABLE tb_estoque ADD CONSTRAINT PK_tb_estoque PRIMARY KEY (cod_prod_est);


CREATE TABLE tb_pop (
 cod_pop CHAR(10) NOT NULL,
 data_pop VARCHAR(10) NOT NULL,
 tarefa_pop VARCHAR(10) NOT NULL,
 responsavel_pop VARCHAR(10) NOT NULL,
 material_pop VARCHAR(10) NOT NULL,
 passos_pop VARCHAR(10) NOT NULL,
 manuseio_pop VARCHAR(10) NOT NULL,
 resul_pop VARCHAR(10) NOT NULL,
 acao_pop VARCHAR(10) NOT NULL,
 cpf VARCHAR(10)
);

ALTER TABLE tb_pop ADD CONSTRAINT PK_tb_pop PRIMARY KEY (cod_pop);


CREATE TABLE tb_professor (
 cpf_prof VARCHAR(10) NOT NULL,
 nome_prof VARCHAR(10) NOT NULL,
 email_prof VARCHAR(10) NOT NULL,
 senha_espec VARCHAR(10) NOT NULL
);

ALTER TABLE tb_professor ADD CONSTRAINT PK_tb_professor PRIMARY KEY (cpf_prof);


CREATE TABLE tb_cadastramento (
 cod_prod VARCHAR(10) NOT NULL,
 descricao_tecnica VARCHAR(10) NOT NULL,
 modelo VARCHAR(10) NOT NULL,
 fabricante VARCHAR(10) NOT NULL,
 num_lote VARCHAR(10) NOT NULL,
 enderecamento VARCHAR(10) NOT NULL,
 cpf_prof VARCHAR(10)
);

ALTER TABLE tb_cadastramento ADD CONSTRAINT PK_tb_cadastramento PRIMARY KEY (cod_prod);


CREATE TABLE tb_expedicao (
 cod_prod_exp VARCHAR(10) NOT NULL,
 desc_exp VARCHAR(10) NOT NULL,
 num_lote_exp VARCHAR(10) NOT NULL,
 quant_exp VARCHAR(10) NOT NULL,
 data_emb_exp VARCHAR(10) NOT NULL,
 respnsavel_exp VARCHAR(10) NOT NULL,
 cpf VARCHAR(10),
 cod_prod VARCHAR(10)
);

ALTER TABLE tb_expedicao ADD CONSTRAINT PK_tb_expedicao PRIMARY KEY (cod_prod_exp);


CREATE TABLE tb_picking (
 cod_produto VARCHAR(10) NOT NULL,
 endereco VARCHAR(10) NOT NULL,
 desc_tecnica VARCHAR(10) NOT NULL,
 modelo_pk VARCHAR(10) NOT NULL,
 fabricante_pk VARCHAR(10) NOT NULL,
 quant_pk INT NOT NULL,
 data_pk INT NOT NULL,
 lote_pk VARCHAR(10) NOT NULL,
 num_picking INT NOT NULL,
 total_pk INT NOT NULL,
 cod_prod VARCHAR(10)
);

ALTER TABLE tb_picking ADD CONSTRAINT PK_tb_picking PRIMARY KEY (cod_produto);


CREATE TABLE tb_rnc (
 desc_nc VARCHAR(10) NOT NULL,
 recebimento VARCHAR(10) NOT NULL,
 num_rnc VARCHAR(10) NOT NULL,
 local_rnc INT NOT NULL,
 quant_entregue INT NOT NULL,
 quant_reprovada INT NOT NULL,
 resp_inspecao VARCHAR(10) NOT NULL,
 cpf VARCHAR(10),
 cod_prod VARCHAR(10)
);

ALTER TABLE tb_rnc ADD CONSTRAINT PK_tb_rnc PRIMARY KEY (desc_nc);


ALTER TABLE tb_estoque ADD CONSTRAINT FK_tb_estoque_0 FOREIGN KEY (cpf) REFERENCES tb_aluno (cpf);


ALTER TABLE tb_pop ADD CONSTRAINT FK_tb_pop_0 FOREIGN KEY (cpf) REFERENCES tb_aluno (cpf);


ALTER TABLE tb_cadastramento ADD CONSTRAINT FK_tb_cadastramento_0 FOREIGN KEY (cpf_prof) REFERENCES tb_professor (cpf_prof);


ALTER TABLE tb_expedicao ADD CONSTRAINT FK_tb_expedicao_0 FOREIGN KEY (cpf) REFERENCES tb_aluno (cpf);
ALTER TABLE tb_expedicao ADD CONSTRAINT FK_tb_expedicao_1 FOREIGN KEY (cod_prod) REFERENCES tb_cadastramento (cod_prod);


ALTER TABLE tb_picking ADD CONSTRAINT FK_tb_picking_0 FOREIGN KEY (cod_prod) REFERENCES tb_cadastramento (cod_prod);


ALTER TABLE tb_rnc ADD CONSTRAINT FK_tb_rnc_0 FOREIGN KEY (cpf) REFERENCES tb_aluno (cpf);
ALTER TABLE tb_rnc ADD CONSTRAINT FK_tb_rnc_1 FOREIGN KEY (cod_prod) REFERENCES tb_cadastramento (cod_prod);


