CREATE DATABASE databaseProfessor;
USE databaseProfessor;

CREATE TABLE tb_professor (
 cod_prof INT NOT NULL AUTO_INCREMENT,
 nome_prof VARCHAR(10) NOT NULL,
 email_prof VARCHAR(10) NOT NULL,
 senha_espec VARCHAR(10) NOT NULL
);

ALTER TABLE tb_professor ADD CONSTRAINT PK_tb_professor PRIMARY KEY (cod_prof);


CREATE TABLE tb_cadastramento (
 cod_prod VARCHAR(10) NOT NULL,
 descricao_tecnica VARCHAR(10) NOT NULL,
 modelo VARCHAR(10) NOT NULL,
 fabricante VARCHAR(10) NOT NULL,
 num_lote VARCHAR(10) NOT NULL,
 enderecamento VARCHAR(10) NOT NULL,
 cod_prof VARCHAR(10) NOT NULL
);

ALTER TABLE tb_cadastramento ADD CONSTRAINT PK_tb_cadastramento PRIMARY KEY (cod_prod);


ALTER TABLE tb_cadastramento ADD CONSTRAINT FK_tb_cadastramento_0 FOREIGN KEY (cod_prof) REFERENCES tb_professor (cod_prof);


