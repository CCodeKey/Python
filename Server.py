import socket

HOST = '10.15.2.96' #IP servidor
PORT = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print()
print('######################    Aguardando Perguntas    ######################')
print()

def envio():
    with open("C:\\Users\\Code Key\\Desktop\\Programas\\ChatGPT\\respotas\\resposta_a.txt","r") as text_A:
        A = str(text_A.read())
    with open("C:\\Users\\Code Key\\Desktop\\Programas\\ChatGPT\\respotas\\resposta_b.txt","r") as text_B:    
        B = str(text_B.read())
    print("A -> ", A)
    print("B -> ", B)
    end = (f"""
Participante  A  ->  {A}

Participante  B  ->  {B}
    """)
    resposta_do_chat = str(end).encode()
    server_socket.sendto(resposta_do_chat, address)

def Pessoa_A(pergunta):
    def fazer_pergunta_no_chat(pergunta):
        print("Pergunta : ", pergunta)
        print()
        print(" Sua resposta !")
        print()
        msg = input(str("> "))
        return msg

    respostaChatGPT = fazer_pergunta_no_chat(pergunta)
    with open("C:\\Users\\Code Key\\Desktop\\Programas\\ChatGPT\\respotas\\resposta_a.txt", "w") as resp:
        resp.write(str(respostaChatGPT))
    envio()
    print("---------   Respostas enviadas   ---------")
    print()
    print()

def Pessoa_B(pergunta):
    HOSTb = '10.15.2.228' #IP - PC Robótica
    PORTb = 12345
    clienteh_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def Recebimento():
        HOSTa = '10.15.2.96' #IP servidor
        PORTa = 29292
        server_socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket2.bind((HOSTa, PORTa))
        print()
        print("---  Aguardando resposta de B !  ---")
        print()
        for i in range(1):
            data, address = server_socket2.recvfrom(1024)
            RESPOSTA_DE_B = data.decode()
            with open("C:\\Users\\Code Key\\Desktop\\Programas\\ChatGPT\\respotas\\resposta_b.txt", "w") as respt:
                respt.write(str(RESPOSTA_DE_B))  
                print("      -- Reposta recebida ! --")  
                print()   

    for i in range(1):
        msg = pergunta
        message = msg.encode()
        clienteh_socket.sendto(message, (HOSTb, PORTb))
        Recebimento()

while True:
    data, address = server_socket.recvfrom(1024)
    print("Usuario   >   ", address)
    print("Pergunta  >   ", data.decode())
    pergunta = data.decode()
    Pessoa_B(pergunta)
    Pessoa_A(pergunta)
