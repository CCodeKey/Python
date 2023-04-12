from flask import request, Flask

partidas = {}
def criar_partida():
    nome_jogador = request.form.get('nome_jogador')

    # Cria uma nova partida e armazena no dicionário de partidas
    nova_partida = {
        'nome_jogador': nome_jogador,
        'jogadores': [nome_jogador],  # Inicialmente, o criador da partida é o único jogador
        # Adicione aqui as informações adicionais da partida, como estado do jogo, pontuação, etc.
    }
    partidas[nome_jogador] = nova_partida