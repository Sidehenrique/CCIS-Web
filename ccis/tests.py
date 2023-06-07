import mysql.connector

# Conectar ao banco de dados
mydb = mysql.connector.connect(
  host="10.6.32.24",
  user="admin",
  password="S1coob4155@@",
  database="database_rh"
)

# Criar um cursor para executar as consultas SQL
mycursor = mydb.cursor()

# Executar a declaração SQL UPDATE para atualizar todas as linhas da coluna "foto"
sql = "UPDATE database_rh.ccis_dadospessoais SET foto = users/avatar.jpg"
val = ("users/avatar.jpg",)  # substitua o valor pelo caminho da foto padrão que você deseja usar
mycursor.execute(sql, val)

# Confirmar as mudanças no banco de dados
mydb.commit()

# Imprimir o número de linhas atualizadas
print(mycursor.rowcount, "linhas atualizadas")

