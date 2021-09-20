#!/usr/bin/env python3
#servidor_UDP.py
#Servidor_UDP
#Lucas Albino Martins
#12011ECP022
#Trabalhao_Sistemas_Distribuidos

import socket

HOST = 'localhost'
PORT = 5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SERVIDOR_UDP = (HOST, PORT)
servidor.bind(SERVIDOR_UDP)
print('Aguardando conexão de um cliente')
Msg_cliente, END_cliente = servidor.recvfrom(1024)

print("Recebi = ",Msg_cliente," , Do cliente", END_cliente)
print('Fechando a conexão')
servidor.close()