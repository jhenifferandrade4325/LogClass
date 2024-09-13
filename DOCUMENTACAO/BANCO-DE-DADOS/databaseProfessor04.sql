CREATE DATABASE databaseProfessor;
USE databaseProfessor;

CREATE TABLE tb_professor (
 cod_prof INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
 nome_prof VARCHAR(100) NOT NULL,
 email_prof VARCHAR(100) NOT NULL,
 senha_espec VARCHAR(100) NOT NULL
);


CREATE TABLE tb_cadastramento (
 cod_prod VARCHAR(100) NOT NULL,
 descricao_tecnica VARCHAR(100) NOT NULL,
 modelo VARCHAR(100) NOT NULL,
 fabricante VARCHAR(100) NOT NULL,
 num_lote VARCHAR(100) NOT NULL,
 enderecamento VARCHAR(100) NOT NULL,
 cod_prof INT NOT NULL
);

ALTER TABLE tb_cadastramento ADD CONSTRAINT PK_tb_cadastramento PRIMARY KEY (cod_prod);


ALTER TABLE tb_cadastramento ADD CONSTRAINT FK_tb_cadastramento_0 FOREIGN KEY (cod_prof) REFERENCES tb_professor (cod_prof);


