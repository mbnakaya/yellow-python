import socket

print("## INICIANDO PORT SCAN ##")

saida=""

while saida!="EXIT":
    host = input("Qual o dominio ou IP do servidor? ")
    port = int(input("Qual porta deseja testar? "))

    obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if obj_socket.connect_ex((host,port)):
        print("Port ", port, " Is closed.")
    else:
        print("Port ", port, " Is open.")

    saida=input("Digite <EXIT> para sair: ").upper()