import socket

HOST = 'localhost' 
PORT = 12345        

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:

    msg = input(str("> "))
    message = msg.encode()
    client_socket.sendto(message, (HOST, PORT))
    data, server_address = client_socket.recvfrom(1024)
    print(f'Resposta do servidor ({server_address}): {data.decode()}')

    # client_socket.close()
