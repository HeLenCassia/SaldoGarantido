from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

saldo = 0

@app.route('/receita', methods=['POST'])
def adicionar_receita():
    global saldo

    dados = request.get_json()

    if 'valor' not in dados:
        return jsonify({"erro": "Campo valor obrigatório"}), 400

    try:
        valor = float(dados['valor'])

        if valor <= 0:
            return jsonify({"erro": "Valor inválido"}), 400

        saldo += valor

        return jsonify({
            "mensagem": "Receita adicionada",
            "saldo": saldo
        }), 200

    except:
        return jsonify({"erro": "Tipo inválido"}), 400

@app.route('/saldo', methods=['GET'])
def consultar_saldo():
    global saldo
    return jsonify({"saldo": saldo})

if __name__ == '__main__':
    app.run(debug=True)