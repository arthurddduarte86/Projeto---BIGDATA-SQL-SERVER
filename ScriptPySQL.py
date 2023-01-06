import pyodbc
import random
from datetime import date

connection_address = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=192.168.0.10;"
    "DATABASE=RegistroVendas;"
    "UID=sa;"
    "PWD=az10ps81@com;"
)
connection = pyodbc.connect(connection_address, autocommit=True)
print("Conexão foi estabelecida -> OK")

cursor = connection.cursor()
id = 0

while id < 100:
    id +=1
    cliente_name = f"Arthur {id}"
    product = f"{id}-{cliente_name}Phone"
    date_of_order = date.today()
    preco = random.randint(3, 5000)
    quantidade = random.randint(1, 20)

    comando = f"""INSERT INTO VENDAS (ID_venda, Cliente, Produto, Data_Venda, Preco, Quantidade) 
    VALUES ({id}, '{cliente_name}', '{product}', '{date_of_order}', {preco}, {quantidade}) """

    print(f"{id} apenas pra saber qual a iteração atual..")
    cursor.execute(comando)
    
cursor.close()




# id = 3
# cliente = "Lira Python"
# produto = "Carro"
# data = "25/08/2021"
# preco = 5000
# quantidade = 1

# comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
# VALUES
#     ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

# cursor.execute(comando)
# cursor.commit()