import socket
import openai


HOST = '10.15.2.96'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

def pesquisar(pergunta):
    openai.api_key = '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'

    def fazer_pergunta_no_chat(pergunta):
        engine = "text-davinci-002"
        prompt = f"Fazer uma pergunta: {pergunta}"
        completions = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=1024)
        resposta = completions.choices[0].text.strip()
        return resposta

    # Exemplo de uso
    respostaChatGPT = fazer_pergunta_no_chat(pergunta)
    print("Resposta do ChatGPT : ", respostaChatGPT)
    # response = f'Resposta do servidor para {address}'.encode()
    respostaChatGPT = respostaChatGPT.encode()
    server_socket.sendto(respostaChatGPT, address)


print('Aguardando Perguntas ...')
print()

while True:
    # Recebe dados e end  ereço do remetente
    data, address = server_socket.recvfrom(1024)
    print("Usuario > ", address)
    print("Pergunta > ", data.decode())
    pesquisar(data.decode())

    # Envia uma resposta para o remetente
    # response = f'Resposta do servidor para {address}'.encode()
    # server_socket.sendto(response, address)
