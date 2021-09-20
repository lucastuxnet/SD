#!/usr/bin/env python3
#cliente_UDP.py
#Conexao_Cliente_UDP
#Lucas Albino Martins
#12011ECP022
#Trabalhao_Sistemas_Distribuidos

import socket

HOST = '127.0.0.1'
PORT = 5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

CONECTAR_SERVIDOR = (HOST, PORT)

Msg_cliente = input("Digite alguma mensagem para ser enviada ao servidor: ")

servidor.sendto(bytes(Msg_cliente,"utf8"), CONECTAR_SERVIDOR)

servidor.close()


