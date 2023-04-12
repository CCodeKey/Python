from flask import Flask, request, jsonify, send_from_directory
# import game_partida

app = Flask(__name__)
jogadores_na_partida = []
partidas = {}


# Rota para receber as ações do jogador

IMAGES_DIR = ('C:\\Users\\Code Key\\Desktop\\Programas\\Game Frenesi\\Servidor  Cliente - Flask\\gato.jpg')
@app.route('/game/imagem')
def mostrar_imagem(nome_imagem):
    try:
        # Envia a imagem do diretório de imagens para o cliente
        return send_from_directory(IMAGES_DIR, nome_imagem)
    except FileNotFoundError:
        return 'Imagem não encontrada', 404

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

@app.route('/criar_partida', methods=['POST'])
def criar_partida():
    nome_jogador = request.form.get('nome_jogador')

    # Cria uma nova partida e armazena no dicionário de partidas
    nova_partida = {
        'nome_jogador': nome_jogador,
        'jogadores': [nome_jogador],  # Inicialmente, o criador da partida é o único jogador
        # Adicione aqui as informações adicionais da partida, como estado do jogo, pontuação, etc.
    }
    partidas[nome_jogador] = nova_partida
    return f'Partida criada por {nome_jogador}'






@app.route('/novaConta', methods=['POST'])
def novo_jogador():
    nome_jogador = request.form.get('nome_jogador')
    senha_jogador = request.form.get('senha_jogador')
    with open("C:\\Users\\Code Key\\Desktop\\Programas\\Game Frenesi\\Servidor  Cliente - Flask\\usuarios\\usuarios.txt", "a") as users:
        users.write(f"\n{nome_jogador} : {senha_jogador}")

    return f'Novo player criado (# {nome_jogador} #)'


def verificar_credenciais(usuario, senha):
    with open("C:\\Users\\Code Key\\Desktop\\Programas\\Game Frenesi\\Servidor  Cliente - Flask\\usuarios\\usuarios.txt","r") as banco:
        for login in banco:
            login = login.strip()
            partes = login.split(' : ')
            if len(partes) == 2 and partes[0] == usuario and partes[1] == senha:
                return True
        return False
@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('nick')
    senha = request.form.get('password')
    if verificar_credenciais(usuario, senha):
    # if usuario in USUARIOS_CADASTRADOS and USUARIOS_CADASTRADOS[usuario] == senha:
        return jsonify(f"Login realizado com sucesso ! Bem Vindo de volta {usuario}")
    else:
        # return jsonify({'status': 'erro', 'mensagem': ' Usuário ou senha inválidos ! '})
        return jsonify("Erro usuario não encontrado !")



    return jsonify(resposta), 200
    # dados_do_jogo = request.json
    # nome = dados_do_jogo.get('nick')
    # senha = dados_do_jogo.get('password')

    # resposta = {
    #     'nome > ':nome,
    #     'senha > ':senha
    # }
    # # with open("C:\\Users\\Code Key\\Desktop\\Programas\\Game Frenesi\\Servidor  Cliente - Flask\\usuarios\\usuarios.txt","r") as login:
    # #     prt = print(login.readlines())

    
    # return jsonify(resposta), 200









@app.route('/game', methods=['POST'])
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
    app.run( host='10.15.2.96', port=5000, debug=True)
    
    
   
# from flask import Flask, request

# app = Flask(__name__)

# # Número a ser adivinhado pelo jogador
# numero_secreto = 42

# @app.route('/adivinhar', methods=['POST'])
# def adivinhar():
#     try:
#         # Obtém o palpite do jogador enviado pelo cliente
#         palpite = int(request.form['palpite'])
        
#         # Compara o palpite com o número secreto
#         if palpite == numero_secreto:
#             return 'Parabéns, você acertou o número!'
#         elif palpite < numero_secreto:
#             return 'Tente novamente, o número é maior.'
#         else:
#             return 'Tente novamente, o número é menor.'
#     except ValueError:
#         return 'Erro: o palpite deve ser um número inteiro.'

# if __name__ == '__main__':
#     app.run(host='10.15.2.96', port=5000)
