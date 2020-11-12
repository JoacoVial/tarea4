import os
import socket
import sys
import codecs
import pickle
from phe import paillier
import time
import subprocess
import hashlib

def descomponer_archivo_1():
    file = open('cracked/crack_1.txt', 'r')
    pass_texto_claro = list()
    archivos = list()
    char = 0
    aux = 0 #auxiliar que observa : y espacios
    password = ""
    for x in file:
        while char < len(x):
            if (aux == 1):
                password += x[char]
            if (x[char] == ":"):
                aux += 1
            char += 1

        archivos.append(password[0: len(password)-1])
        password = ""
        aux = 0
        char = 0

    file.close()
    return archivos

def descomponer_archivo_2():
    file = open('cracked/crack_2.txt', 'r')
    pass_texto_claro = list()
    archivos = list()
    char = 0
    aux = 0 #auxiliar que observa : y espacios
    password = ""
    for x in file:
        while char < len(x):
            if (aux == 2):
                password += x[char]
            if (x[char] == ":"):
                aux += 1
            char += 1

        archivos.append(password[0: len(password)-1])
        password = ""
        aux = 0
        char = 0

    file.close()
    return archivos

def descomponer_archivo_3():
    file = open('cracked/crack_3.txt', 'r')
    pass_texto_claro = list()
    char = 0
    aux = 0 #auxiliar que observa : y espacios
    password = ""
    archivos = list()
    for x in file:
        while char < len(x):
            if (aux == 2):
                password += x[char]
            if (x[char] == ":"):
                aux += 1
            char += 1

        archivos.append(password[0: len(password)-1])
        password = ""
        aux = 0
        char = 0

    file.close()
    return archivos

def descomponer_archivo_4():
    file = open('cracked/crack_4.txt', 'r')
    pass_texto_claro = list()
    char = 0
    aux = 0 #auxiliar que observa : y espacios
    password = ""
    archivos = list()
    for x in file:
        while char < len(x):
            if (aux == 1):
                password += x[char]
            if (x[char] == ":"):
                aux += 1
            char += 1

        archivos.append(password[0: len(password)-1])
        password = ""
        aux = 0
        char = 0

    file.close()
    return archivos

def descomponer_archivo_5():
    file = open('cracked/crack_5.txt', 'r')
    pass_texto_claro = list()
    char = 0
    aux = 0 #auxiliar que observa : y espacios
    password = ""
    archivos = list()
    for x in file:
        while char < len(x):
            if (aux == 1):
                password += x[char]
            if (x[char] == ":"):
                aux += 1
            char += 1

        archivos.append(password[0: len(password)-1])
        password = ""
        aux = 0
        char = 0

    file.close()
    return archivos

def write_file(archivo_encriptado):
    file = open('archivo_encriptado.txt', 'w')

    for password in archivo_encriptado:
        file.write(str(password) + "\n")

    file.close()

def encriptar_archivo(archivo, public_key, sock):
    archivo_encriptado = list()
    password_aux= ""
    largo = len(archivo)
    pos = 0

    t_inicial_archivo = time.time()

    for password in archivo:
        password_aux = codecs.encode(password.encode(), "hex")
        password_aux = str(password_aux, 'utf-8')
        password_aux = int(password_aux,16)

        encrypted_number = public_key.encrypt(password_aux)
        archivo_encriptado.append(encrypted_number)
        password_aux = ""

        if(((100*pos)/largo) % 4 == 0):
            print("Vamos en ", (100*pos)/largo, "%")
            sock.send(b'Test')
        pos+=1

    t_final_archivo = time.time()
    print("El cifrado demora ", t_final_archivo - t_inicial_archivo, "segundos.")

    return archivo_encriptado

def sha3(archivo):
    t_inicial_archivo = time.time()
    s = hashlib.sha3_512()
    archivo_hash = list()
    for i in archivo:
        s.update(i.encode('utf-8'))
        archivo_hash.append(s.hexdigest())
    t_final_archivo = time.time()
    print("Demora:", t_final_archivo - t_inicial_archivo)
    return archivo_hash

class ProcessData:
    process_id = 0
    project_id = 0
    task_id = 0
    start_time = 0
    end_time = 0
    user_id = 0
    weekend_id = 0

t_inicial_archivo = time.time()
os.system("hashcat.exe -m 0 -a 0 -D 2 -o cracked/crack_1.txt archivos/archivo_1 diccionarios/diccionario_1.dict diccionarios/diccionario_2.dict")
t_final_archivo = time.time()
tiempo_1= t_final_archivo - t_inicial_archivo

t_inicial_archivo = time.time()
os.system("hashcat.exe -m 10 -a 0 -D 2 -o cracked/crack_2.txt archivos/archivo_2 diccionarios/diccionario_1.dict diccionarios/diccionario_2.dict")
t_final_archivo = time.time()
tiempo_2 = t_final_archivo - t_inicial_archivo

t_inicial_archivo = time.time()
os.system("hashcat.exe -m 10 -a 0 -D 2 -o cracked/crack_3.txt archivos/archivo_3 diccionarios/diccionario_1.dict diccionarios/diccionario_2.dict")
t_final_archivo = time.time()
tiempo_3= t_final_archivo - t_inicial_archivo

t_inicial_archivo = time.time()
os.system("hashcat.exe -m 1000 -a 0 -D 2 -o cracked/crack_4.txt archivos/archivo_4 diccionarios/diccionario_1.dict diccionarios/diccionario_2.dict")
t_final_archivo = time.time()
tiempo_4= t_final_archivo - t_inicial_archivo

t_inicial_archivo = time.time()
os.system("hashcat.exe -m 1800 -a 0 -D 2 -o cracked/crack_5.txt archivos/archivo_5 diccionarios/diccionario_1.dict diccionarios/diccionario_2.dict")
t_final_archivo = time.time()
tiempo_5= t_final_archivo - t_inicial_archivo

print("\n--------------------------------------------")
print("Tiempo en crackear archivo 1: " + str(tiempo_1))
print("Tiempo en crackear archivo 2: " + str(tiempo_2))
print("Tiempo en crackear archivo 3: " + str(tiempo_3))
print("Tiempo en crackear archivo 4: " + str(tiempo_4))
print("Tiempo en crackear archivo 5: " + str(tiempo_5))

print("\n--------------------------------------------")
archivo1 = descomponer_archivo_1()
archivo2 = descomponer_archivo_2()
archivo3 = descomponer_archivo_3()
archivo4 = descomponer_archivo_4()
archivo5 = descomponer_archivo_5()
print("Largo archivo 1:", len(archivo1))
print("Largo archivo 2:", len(archivo2))
print("Largo archivo 3:", len(archivo3))
print("Largo archivo 4:", len(archivo4))
print("Largo archivo 5:", len(archivo5))

archivos= archivo1 + archivo2 + archivo3 + archivo4 + archivo5

print("\n--------------------------------------------")
print("Tiempo en hashear archivo 1: ")
archivo1_sha3 = sha3(archivo1)
print("Tiempo en hashear archivo 2: ")
archivo2_sha3 = sha3(archivo2)
print("Tiempo en hashear archivo 3: ")
archivo3_sha3 = sha3(archivo3)
print("Tiempo en hashear archivo 4: ")
archivo4_sha3 = sha3(archivo4)
print("Tiempo en hashear archivo 5: ")
archivo5_sha3 = sha3(archivo5)

archivos_sha3 = archivo1_sha3 + archivo2_sha3 + archivo3_sha3 + archivo4_sha3 + archivo5_sha3

subprocess.Popen("python servidor.py 1", shell=True)

time.sleep(3)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print("\n--------------------------------------------")
print('Conectandose a {} puerto {}'.format(*server_address))
sock.connect(server_address)

time.sleep(1)

data = sock.recv(4096)
public_key = pickle.loads(data)

archivo_encriptado = list()
print("\n--------------------------------------------")
print("Encriptando archivo 1:")
archivo1_encriptado = encriptar_archivo(archivo1_sha3, public_key, sock)
print("\n--------------------------------------------")
print("Encriptando archivo 2:")
archivo2_encriptado = encriptar_archivo(archivo2_sha3, public_key, sock)
print("\n--------------------------------------------")
print("Encriptando archivo 3:")
archivo3_encriptado = encriptar_archivo(archivo3_sha3, public_key, sock)
print("\n--------------------------------------------")
print("Encriptando archivo 4:")
archivo4_encriptado = encriptar_archivo(archivo4_sha3, public_key, sock)
print("\n--------------------------------------------")
print("Encriptando archivo 5:")
archivo5_encriptado = encriptar_archivo(archivo5_sha3, public_key, sock)

archivo_encriptado = archivo1_encriptado + archivo2_encriptado + archivo3_encriptado + archivo4_encriptado + archivo5_encriptado
write_file(archivo_encriptado)

sock.send(b'Puedes recibir')
time.sleep(0.01)
for i in archivo_encriptado:
    data = pickle.dumps(i)
    sock.send(data)
    time.sleep(0.01)
sock.send(b'Listo')
data = sock.recv(4096)
print(data)
