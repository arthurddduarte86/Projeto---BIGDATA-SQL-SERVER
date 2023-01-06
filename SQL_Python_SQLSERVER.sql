/* 
Comando abaixo já executado
CREATE TABLE VENDAS (ID_venda INT, Cliente VARCHAR(50), Produto VARCHAR(100), Data_Venda DATE, Preco DECIMAL(6, 2), Quantidade INT)

*/

INSERT INTO VENDAS (ID_venda, Cliente, Produto, Data_Venda, Preco, Quantidade)
VALUES (1, 'Arthur', 'Caneca', '05/01/2023', 24, 3)
SELECT * FROM VENDAS