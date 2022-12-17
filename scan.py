import socket

print("## INICIANDO PORT SCAN ##")
host = input("Qual o dominio ou IP do servidor? ")

for port in range(0, 1024):
    obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if obj_socket.connect_ex((host, port)):
        print("Porta ", port, " fechada.")
    else:
        print("Porta ", port, " aberta.")