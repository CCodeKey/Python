import socket

HOST = '10.15.2.96' #IP servidor
PORT = 12345       
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input(str("> "))
    message = msg.encode()
    client_socket.sendto(message, (HOST, PORT))
    data, server_address = client_socket.recvfrom(1024)
    print(f'Resposta do servidor : {data.decode()}')
    print()
