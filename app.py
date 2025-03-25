from flask import Flask, jsonify
import random

app = Flask(__name__)

charadas = [
    {'id': 1, 'charada': 'Por que o computador foi ao médico?', 'resposta': 'Porque ele estava com um vírus.'},
    {'id': 2, 'charada': 'O que é um vegetariano que come carne?', 'resposta': 'Um ex-vegetariano.'},
    {'id': 3, 'charada': 'Como o oceano diz olá?', 'resposta': 'Ele acena.'},
    {'id': 4, 'charada': 'Por que os pássaros não usam Facebook?', 'resposta': 'Porque já têm Twitter.'},
    {'id': 5, 'charada': 'O que é pequeno e vermelho, mas não é uma maçã?', 'resposta': 'Um tomate com raiva.'},
    {'id': 6, 'charada': 'O que acontece quando uma vaca pula sobre uma cerca?', 'resposta': 'A gacha é feita!'},
    {'id': 7, 'charada': 'O que a banana falou para o tomate?', 'resposta': 'Você é muito maduro!'},
    {'id': 8, 'charada': 'O que é um ponto vermelho no canto da sala?', 'resposta': 'Um tomate se escondendo!'},
    {'id': 9, 'charada': 'Por que o lápis não pode ir para a escola?', 'resposta': 'Porque ele já estava apontado!'},
    {'id': 10, 'charada': 'O que você chama um boomerangue que não volta?', 'resposta': 'Um pedaço de pau!'},
    {'id': 11, 'charada': 'O que é verde e fica em cima da árvore?', 'resposta': 'Uma rã de bicicleta!'},
    {'id': 12, 'charada': 'O que você chama de um cachorro que faz mágica?', 'resposta': 'Um labracadabrador!'},
    {'id': 13, 'charada': 'Por que os esqueletos não brigam entre si?', 'resposta': 'Porque eles não têm coragem!'},
    {'id': 14, 'charada': 'Como a geladeira se apresenta?', 'resposta': 'Ela diz: Estou cheia de gelo!'},
    {'id': 15, 'charada': 'O que é um gato com um cinto?', 'resposta': 'Um cinturato!'}
]

@app.route('/')
def index():
    return 'Charada ta ON!'

@app.route('/charadas', methods=['GET'])
def charada():
    charada_aleatoria = random.choice(charadas)
    return (f"Charada:\n{charada_aleatoria}")  

@app.route('/charadas/<int:id>', methods=['GET'])
def busca(id):
    for charada in charadas:
        if charada['id'] == id:
            return jsonify(charada), 200

    return jsonify({'mensagem':'ERRO! Charada não encontrado'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)