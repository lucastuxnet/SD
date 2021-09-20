#!/usr/bin/env python3
#cliente_tcp.py
#Conexao_Cliente_TCP
#Lucas Albino Martins
#12011ECP022
#Trabalhao_Sistemas_Distribuidos

import socket

HOST = '127.0.0.1'
PORT = 50001

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.connect((HOST, PORT))
servidor.sendall(str.encode('Cliente conectou corretamente no servidor.'))
data = servidor.recv(1024)

print('Conexão bem sucedida:', data.decode())
