import socket
HOST = '10.15.2.237'
PORT = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print('Aguardando Perguntas ...')
print()

def enviar_resposta():
    HOST = '10.15.2.96' 
    PORT = 29292        
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(1):
        print()
        print(" Sua resposta !")
        print()
        msg = input(str("> "))
        resposta = msg.encode()
        client_socket.sendto(resposta, (HOST,PORT))

while True:
    data, address = server_socket.recvfrom(1024)
    print("Pergunta : ", data.decode())
    enviar_resposta()