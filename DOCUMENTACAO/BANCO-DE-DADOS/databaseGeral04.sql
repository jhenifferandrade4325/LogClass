CREATE DATABASE turma3;
USE turma3;

CREATE USER 'usuario_logclass'@'%' IDENTIFIED BY 'logclass';

GRANT ALL PRIVILEGES ON *.* TO 'usuario_logclass'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;

CREATE TABLE tb_aluno (
 cod_aluno INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
 nome VARCHAR(100) NOT NULL,
 email VARCHAR(100) NOT NULL,
 senha VARCHAR(100) NOT NULL
);



CREATE TABLE tb_cadastramento (
 cod_prod VARCHAR(100) NOT NULL,
 descricao_tecnica VARCHAR(100) NOT NULL,
 modelo VARCHAR(100) NOT NULL,
 fabricante VARCHAR(100) NOT NULL,
 num_lote VARCHAR(100) NOT NULL,
 enderecamento VARCHAR(100) NOT NULL
);

ALTER TABLE tb_cadastramento ADD CONSTRAINT PK_tb_cadastramento PRIMARY KEY (cod_prod);


CREATE TABLE tb_estoque (
 cod_prod_est INT NOT NULL,
 num_lote_est INT NOT NULL,
 loc_est CHAR(100) NOT NULL,
 desc_tec VARCHAR(100) NOT NULL,
 data_entrega INT NOT NULL,
 quant_itens_entrada INT NOT NULL,
 data_saida INT NOT NULL,
 quant_saida INT NOT NULL,
 saldo INT NOT NULL,
 func_responsavel VARCHAR(100) NOT NULL,
 cod_aluno INT NOT NULL
);

ALTER TABLE tb_estoque ADD CONSTRAINT PK_tb_estoque PRIMARY KEY (cod_prod_est);


CREATE TABLE tb_expedicao (
 cod_prod_exp VARCHAR(100) NOT NULL,
 desc_exp VARCHAR(100) NOT NULL,
 num_lote_exp VARCHAR(100) NOT NULL,
 quant_exp VARCHAR(100) NOT NULL,
 data_emb_exp VARCHAR(100) NOT NULL,
 respnsavel_exp VARCHAR(100) NOT NULL,
 cod_prod VARCHAR(100) NOT NULL,
 cod_aluno INT NOT NULL
);

ALTER TABLE tb_expedicao ADD CONSTRAINT PK_tb_expedicao PRIMARY KEY (cod_prod_exp);


CREATE TABLE tb_picking (
 cod_produto VARCHAR(100) NOT NULL,
 endereco VARCHAR(100) NOT NULL,
 desc_tecnica VARCHAR(100) NOT NULL,
 modelo_pk VARCHAR(100) NOT NULL,
 fabricante_pk VARCHAR(100) NOT NULL,
 quant_pk INT NOT NULL,
 data_pk INT NOT NULL,
 lote_pk VARCHAR(100) NOT NULL,
 num_picking INT NOT NULL,
 total_pk INT NOT NULL,
 cod_prod VARCHAR(100) NOT NULL
);

ALTER TABLE tb_picking ADD CONSTRAINT PK_tb_picking PRIMARY KEY (cod_produto);


CREATE TABLE tb_pop (
 cod_pop CHAR(100) NOT NULL,
 data_pop VARCHAR(100) NOT NULL,
 tarefa_pop VARCHAR(100) NOT NULL,
 responsavel_pop VARCHAR(100) NOT NULL,
 material_pop VARCHAR(100) NOT NULL,
 passos_pop VARCHAR(100) NOT NULL,
 manuseio_pop VARCHAR(100) NOT NULL,
 resul_pop VARCHAR(100) NOT NULL,
 acao_pop VARCHAR(100) NOT NULL,
 cod_aluno INT NOT NULL
);

ALTER TABLE tb_pop ADD CONSTRAINT PK_tb_pop PRIMARY KEY (cod_pop);


CREATE TABLE tb_rnc (
 desc_rnc VARCHAR(100) NOT NULL,
 recebimento VARCHAR(100) NOT NULL,
 num_rnc VARCHAR(100) NOT NULL,
 local INT NOT NULL,
 quant_entregue INT NOT NULL,
 quant_reprovada INT NOT NULL,
 resp_inspecao VARCHAR(100) NOT NULL,
 cod_prod VARCHAR(100) NOT NULL,
 cod_aluno INT NOT NULL
);

ALTER TABLE tb_rnc ADD CONSTRAINT PK_tb_rnc PRIMARY KEY (desc_rnc);


ALTER TABLE tb_estoque ADD CONSTRAINT FK_tb_estoque_0 FOREIGN KEY (cod_aluno) REFERENCES tb_aluno (cod_aluno);


ALTER TABLE tb_expedicao ADD CONSTRAINT FK_tb_expedicao_0 FOREIGN KEY (cod_prod) REFERENCES tb_cadastramento (cod_prod);
ALTER TABLE tb_expedicao ADD CONSTRAINT FK_tb_expedicao_1 FOREIGN KEY (cod_aluno) REFERENCES tb_aluno (cod_aluno);


ALTER TABLE tb_picking ADD CONSTRAINT FK_tb_picking_0 FOREIGN KEY (cod_prod) REFERENCES tb_cadastramento (cod_prod);


ALTER TABLE tb_pop ADD CONSTRAINT FK_tb_pop_0 FOREIGN KEY (cod_aluno) REFERENCES tb_aluno (cod_aluno);


ALTER TABLE tb_rnc ADD CONSTRAINT FK_tb_rnc_0 FOREIGN KEY (cod_prod) REFERENCES tb_cadastramento (cod_prod);
ALTER TABLE tb_rnc ADD CONSTRAINT FK_tb_rnc_1 FOREIGN KEY (cod_aluno) REFERENCES tb_aluno (cod_aluno);


