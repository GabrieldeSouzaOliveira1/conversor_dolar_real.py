import requests  # Importa a biblioteca requests para fazer requisições HTTP

# URL da API que fornece a cotação do dólar para real
url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

# Faz uma requisição GET para a API
response = requests.get(url)

# Converte a resposta JSON para um dicionário Python
data = response.json()

# Obtém o valor de compra do dólar (campo "bid")
cotacao = float(data["USDBRL"]["bid"])
