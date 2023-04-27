import socket
import openai

HOST = '10.15.2.96'
PORT = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print('Aguardando Perguntas ...')
print()

def envio():
    with open("C:\\Users\\Code Key\\Desktop\\Programas\\ChatGPT\\respotas\\resposta_a.txt","r") as text_A:
        with open("C:\\Users\\Code Key\\Desktop\\Programas\\ChatGPT\\respotas\\resposta_b.txt","r") as text_B:
            A = text_A.read()
            B = text_B.read()
            print("A -> ", A)
            print("B ->", B)
    end = (f"""
Participante  A  ->  {A}


Participante  B  ->  {B}
    """)
    resposta_do_chat = str(end).encode()
    server_socket.sendto(resposta_do_chat, address)

def Pessoa_A(pergunta):
    openai.api_key = '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'

    def fazer_pergunta_no_chat(pergunta):
        engine = "text-davinci-002"
        prompt = f"Fazer uma pergunta: {pergunta}"
        completions = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=1024)
        respostaCHT = completions.choices[0].text.strip()
        return respostaCHT

    respostaChatGPT = fazer_pergunta_no_chat(pergunta)
    with open("C:\\Users\\Code Key\\Desktop\\Programas\\ChatGPT\\respotas\\resposta_a.txt", "w") as resp:
        resp.write(respostaChatGPT)

def Pessoa_B(pergunta):
    HOSTb = '10.15.2.237'
    PORTb = 12345
    clienteh_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def Recebimento():
        HOSTa = '10.15.2.96' 
        PORTa = 29292
        server_socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket2.bind((HOSTa, PORTa))
        print("Esperando resposta !")
        print()
        for i in range(1):
            data, address = server_socket2.recvfrom(1024)
            RESPOSTA_DE_B = data.decode()
            # envio_de_respostas_b(RESPOSTA_DE_B)
            with open("C:\\Users\\Code Key\\Desktop\\Programas\\ChatGPT\\respotas\\resposta_b.txt", "w") as respt:
                respt.write(RESPOSTA_DE_B)
                envio()        

    for i in range(1):
        msg = pergunta
        message = msg.encode()
        clienteh_socket.sendto(message, (HOSTb, PORTb))
        Recebimento()

while True:
    data, address = server_socket.recvfrom(1024)
    print("Usuario > ", address)
    print("Pergunta > ", data.decode())
    pergunta = data.decode()
    Pessoa_B(pergunta)
    Pessoa_A(pergunta)
