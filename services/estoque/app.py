# services/estoque/app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reservar', methods=['POST'])
def reservar_estoque():
    dados = request.json
    correlation_id = dados.get('correlation_id')
    item = dados.get('item')

    print(f"[{correlation_id}] Verificando estoque para: {item}")
    
    # Aqui entraria a lógica de banco de dados
    return jsonify({"status": "Reservado"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)