# import requests
# # URL do servidor Flask
# url = 'http://10.15.2.96:5000/game'

# # Dados do jogo a serem enviados
# dados_do_jogo = {
#     'acao': 'mover',
#     'direcao': 'esquerda',
#     'velocidade': 5
# }

# jogador={
# 	'nome':'JOGADOR !'
# }
# jogador['nome'] = input("Digite o nome do jogador > ")
# # Loop principal do cliente
# while True:
#     # Envia uma requisição POST para o servidor Flask com os dados do jogo
   
#     pplayer =  requests.post(url, json=jogador)
#     response = requests.post(url, json=dados_do_jogo)

#     # Verifica a resposta do servidor
#     if response.status_code == 200:
#         resposta = response.json()
#         print("Resposta do servidor:", resposta)
#     else:
#         print("Erro ao se comunicar com o servidor. Código de resposta:", response.status_code)

    # Implemente a lógica do jogo aqui
    # Atualize os dados do jogo no cliente
    # Receba atualizações do estado do jogo do servidor
    # Envie ações do jogador para o servidor

    # Exemplo de espera de um tempo antes de fazer a próxima requisição
    # Você pode ajustar o tempo de espera de acordo com a velocidade do jogo
    
    
    
#     dados_do_jogo['velocidade'] = input("Digite a velocidade > ")

















# import requests

# # URL do servidor Flask
# url_servidor = 'http://10.15.2.96:5000'

# # Dados do jogador que está criando a partida
# nome_jogador = input("Digite seu nome > ")

# # Envia a requisição para criar a partida
# resposta = requests.post(f'{url_servidor}/criar_partida', data={'nome_jogador': nome_jogador})

# # Verifica a resposta do servidor
# if resposta.status_code == 200:
#     print(f'Partida criada com sucesso por {nome_jogador}')
# else:
#     print(f'Erro ao criar a partida: {resposta.text}')
import requests
url_servidor = 'http://10.15.2.96:5000'


def login():
    print()
    print()
    nick = input("NICK > ")
    password = input("PASSWORD > ")
    rodada = {
        'nick': nick,
        'password': password
    }
    response = requests.post(f"{url_servidor}/login", data=rodada)

    # Verifica a resposta do servidor
    if response.status_code == 200:
        resposta = response.json()
        print()
        print(resposta)
        print()
    else:
        print()
        print(f"Erro ao efetuar o login no Servidor > { response.status_code }")
        print()




    # resposta = requests.get(f'{url_servidor}/login', data={
    #     'nick': nick,
    #     'password': password
    # })
    # if resposta.status_code == 200:
    #     print(f'Bem Vindo de Volta {nick} !')
    #     # login()
    # else:
    #     print(f'Erro ao efetuar o login no Servidor > {resposta.text}')


def nova_conta():
    # Dados do jogador que está criando a partida
    nome_jogador = input("Digite o nick do Jogador > ")
    senha_jogador = input("Digite a senha do Jogador > ")

    # Envia a requisição para criar a partida
    resposta = requests.post(f'{url_servidor}/novaConta', data={
        'nome_jogador': nome_jogador,
        'senha_jogador': senha_jogador
    })
    if resposta.status_code == 200:
        print(f'Nova conta criada, seja bem vindo {nome_jogador} !')
        login()
    else:
        print(f'Erro ao criar sua conta: {resposta.text}')


# nova_conta()


















# import requests

# # URL do servidor Flask
# url_servidor = 'http://10.15.2.96:5000'

# # Loop para o jogador tentar adivinhar o número
# while True:
#     palpite = input('Digite um número entre 1 e 100: ')
#     resposta = requests.post(f'{url_servidor}/adivinhar', data={'palpite': palpite})
#     print(resposta.text)
