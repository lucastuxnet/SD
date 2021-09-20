#!/usr/bin/env python3
#servidor_TCP.py
#Servidor_TCP
#Lucas Albino Martins
#12011ECP022
#Trabalhao_Sistemas_Distribuidos

import socket

HOST = 'localhost'
PORT = 50001

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print('Aguardando conexão de um cliente')
conn, ender = servidor.accept()

print('Conectado em', ender)
while True:
    data = conn.recv(1024)
    if not data:
        print('Fechando a conexão')
        conn.close()
        break
    conn.sendall(data)
