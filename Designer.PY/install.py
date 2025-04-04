import mysql.connector

 
def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database= "meu_banco"
        )


def adicionar_user(login,senha):
    conexao= conectar()
    cursor =conexao.cursor()
    sql= "insert into usuarios (email,senha_hash) values (%s,sha2(%s,256))" # sha2 senha com priptografia
    valores=(login,senha) 
    cursor.execute(sql,valores)
    conexao.commit()
    cursor.close()
    conexao.close()

