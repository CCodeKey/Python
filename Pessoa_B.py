import socket
HOST = '10.15.2.237' # IP da maquína local
PORT = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print()
print('Aguardando Perguntas ...')
print()

def enviar_resposta():
    HOST = '10.15.2.96' #IP servidor
    PORT = 29292        
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(1):
        print()
        print("  Sua resposta !")
        print()
        msg = input(str("> "))
        resposta = msg.encode()
        client_socket.sendto(resposta, (HOST,PORT))
        print("---  Resposta enviada !  ---")
        print()

while True:
    data, address = server_socket.recvfrom(1024)
    print("Pergunta : ", data.decode())
    enviar_resposta()
