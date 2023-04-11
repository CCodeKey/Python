from flask import Flask, request, jsonify


app = Flask(__name__)
jogadores_na_partida = []

# Rota para receber as ações do jogador
@app.route('/game', methods=['POST'])
@app.route('/game/register', methods=['POST'])

def register():
    # Obtém o nome do jogador enviado pelo cliente
    nome_jogador = request.json.get('nome')

    # Adiciona o jogador à lista de jogadores na partida
    jogadores_na_partida.append(nome_jogador)

    # Exemplo de resposta do servidor para o cliente
    resposta = {
        'mensagem': 'Jogador registrado com sucesso',
        'jogadores_na_partida': jogadores_na_partida
    }
    return jsonify(resposta), 200
    
    
@app.route('/game/players', methods=['GET'])
def players():
    # Exemplo de resposta do servidor para o cliente
    resposta = {
        'jogadores_na_partida': jogadores_na_partida
    }

    return jsonify(resposta), 200

def game():
    # Obtém os dados do jogo enviados pelo cliente
    dados_do_jogo = request.json

    # Processa as ações do jogador
    acao = dados_do_jogo.get('acao')
    direcao = dados_do_jogo.get('direcao')
    velocidade = dados_do_jogo.get('velocidade')

    # Implemente a lógica do jogo aqui
    # Atualize o estado do jogo
    # Responda com atualizações apropriadas para o cliente

    # Exemplo de resposta do servidor para o cliente
    resposta = {
        'mensagem': 'Ação do jogador recebida com sucesso',
        'acao': acao,
        'direcao': direcao,
        'velocidade': velocidade
    }

    return jsonify(resposta), 200

if __name__ == '__main__':
    app.run(debug=True)
    
    
   

