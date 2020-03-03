# Coloque aqui o código do teu cliente em Python

#Passo 1:
# Buscar de uma fila de pedidos de empréstimo
# Fila está disponível por GET em:
#https://us-central1-emf-teacher.cloudfunctions.net/function-aulas-getclient
#Parâmetro qtde permite buscar mais de um cliente da fila
# Exibir em tela os clientes da fila

#Passo 2:
# Chamar o teu micro serviço cognitivo
# Exibir em tela a resposta do teu serviço de crédito

# Extra: Opcional
# Gravar em arquivo CSV sequencial

import requests
import pandas as pd

if __name__ == "__main__":
    headers = {'Content-Type': 'application/json'}

    url_clients = 'https://us-central1-emf-teacher.cloudfunctions.net/function-aulas-getclient?qtde=5'
    persons = requests.request("GET", url_clients, headers=headers)

    url = "http://localhost:8080/modelo02"
    response = requests.request("POST", url, headers=headers, data=persons)
    print("Resposta da API:")
    print(response.text.encode('utf8').decode())
    pass