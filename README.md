# Cafeteria Distribuída - Middleware Project

Nossa proposta de projeto consiste em uma aplicação de cafeteria é divida em microsserviços. Utilizando docker, Python e REST ou RPC(ainda vamos decidir)

## Escopo do Projeto
O domínio escolhido é o de uma cafeteria online, dividida em três frentes principais:
* **Cardápio:** Catálogo de produtos e preços.
* **Carrinho:** Gerenciamento de itens selecionados.
* **Pagamento:** Processamento e finalização do pedido.

## Requisitos de Middleware (Obrigatórios)
Para atender à rubrica da disciplina, o sistema implementa as seguintes capacidades

* **Comunicação Síncrona:** Integração via REST ou gRPC entre pelo menos dois serviços.
* **Comunicação Assíncrona:** Uso de mensageria (Fila ou Pub/Sub) em um fluxo crítico (ex: envio do pedido para o pagamento).
* **Resiliência:** Implementação de mecanismos como *Retry*, *Timeout* ou *Circuit Breaker*
* **Observabilidade:** Logs estruturados, métricas básicas e propagação de **Correlation ID** entre os serviços.
* **Segurança:** Autenticação via Token/JWT e autorização por papéis (RBAC).
* **Tolerância a Falhas:** Estratégia documentada para comportamento do sistema em caso de queda de serviços.
