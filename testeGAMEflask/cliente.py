import requests
# URL do servidor Flask
url = 'http://localhost:5000/game'

# Dados do jogo a serem enviados
dados_do_jogo = {
    'acao': 'mover',
    'direcao': 'esquerda',
    'velocidade': 5
}

jogador={
	'nome':'JOGADOR !'
}
jogador['nome'] = input("Digite o nome do jogador > ")
# Loop principal do cliente
while True:
    # Envia uma requisição POST para o servidor Flask com os dados do jogo
   
    pplayer =  requests.post(url, json=jogador)
    response = requests.post(url, json=dados_do_jogo)

    # Verifica a resposta do servidor
    if response.status_code == 200:
        resposta = response.json()
        print("Resposta do servidor:", resposta)
    else:
        print("Erro ao se comunicar com o servidor. Código de resposta:", response.status_code)

    # Implemente a lógica do jogo aqui
    # Atualize os dados do jogo no cliente
    # Receba atualizações do estado do jogo do servidor
    # Envie ações do jogador para o servidor

    # Exemplo de espera de um tempo antes de fazer a próxima requisição
    # Você pode ajustar o tempo de espera de acordo com a velocidade do jogo
    
    
    
    dados_do_jogo['velocidade'] = input("Digite a velocidade > ")

