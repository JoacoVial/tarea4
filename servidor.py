import socket
import sys
import codecs
import pickle
from phe import paillier
import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('JoaquinVial.db')
        return con

    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE password(id integer PRIMARY KEY, hash text)")
    con.commit()

def sql_insert_all(con, archivo):
    id = 0
    for i in archivo:
        password = (id , i)
        cursorObj = con.cursor()
        cursorObj.execute('INSERT INTO password(id, hash) VALUES(?, ?)', password)
        con.commit()
        id +=1

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM password')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

def desencriptar_archivos(archivo, private_key):
    decrypted_number = None
    archivos_desencriptados = list()
    for i in archivo:
        decrypted_number = private_key.decrypt(i)
        decrypted_number = hex(decrypted_number)
        decrypted_number = decrypted_number[2:].encode('utf-8')
        decrypted_number = codecs.decode(decrypted_number, "hex")
        archivos_desencriptados.append(decrypted_number)

    return archivos_desencriptados


class ProcessData:
    process_id = 0
    project_id = 0
    task_id = 0
    start_time = 0
    end_time = 0
    user_id = 0
    weekend_id = 0


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
print("\n--------------------------------------------")
print('Servidor en {} puerto {}'.format(*server_address))
sock.bind(server_address)

public_key, private_key = paillier.generate_paillier_keypair()
variable = ProcessData()
public_key_bytes = pickle.dumps(public_key)

sock.listen(1)

while True:
    print('Servidor esperando conexion')
    connection, client_address = sock.accept()
    if(connection):
        print('Conexion de', client_address)
        connection.send(public_key_bytes)
        archivos_encriptado = list()
        recibir = False
        while 1:
            data = connection.recv(4096)
            if (data == b'Puedes recibir'):
                print("Recibiendo archivo")
                recibir = True
                break

        while recibir:
            data = connection.recv(32768)
            if data == b'Listo':
                break
            else:
                archivos_encriptado.append(pickle.loads(data))
                data = None

        archivos_desencriptados = desencriptar_archivos(archivos_encriptado, private_key)

        con = sql_connection()
        sql_table(con)
        sql_insert_all(con, archivos_desencriptados)

        connection.send(b'Archivos desencriptados')
        break

connection.close()
