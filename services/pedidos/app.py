# services/pedidos/app.py
from flask import Flask, request, jsonify
import requests
import uuid

app = Flask(__name__)

# Simulação de banco de dados
pedidos = []

@app.route('/pedido', methods=['POST'])
def criar_pedido():
    # 1. GERANDO OBSERVABILIDADE (Correlation ID)
    correlation_id = str(uuid.uuid4())
    dados = request.json
    item = dados.get('item')

    print(f"[{correlation_id}] Recebendo pedido de: {item}")

    # 2. COMUNICAÇÃO SÍNCRONA COM MIDDLEWARE DE RESILIÊNCIA (RETRY)
    tentativas = 3
    sucesso = False
    
    for i in range(tentativas):
        try:
            print(f"[{correlation_id}] Tentativa {i+1} de reservar estoque...")
            # Chama o serviço de estoque (que estará no Docker)
            resposta = requests.post(
                'http://servico-estoque:5001/reservar', 
                json={'item': item, 'correlation_id': correlation_id},
                timeout=2 # Timeout para não travar
            )
            if resposta.status_code == 200:
                sucesso = True
                break
        except:
            print(f"[{correlation_id}] Falha na comunicação. Tentando novamente...")

    if sucesso:
        return jsonify({"status": "Pedido Confirmado", "id": correlation_id}), 201
    else:
        return jsonify({"status": "Erro", "msg": "Serviço de estoque indisponível"}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)