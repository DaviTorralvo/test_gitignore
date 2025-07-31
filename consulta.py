import os
import requests

api_key = os.environ.get("API_KEY")


url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

response = requests.get(url)


if response.status_code == 200:
    dados = response.json()
    print(dados)
else:
    print("não achei droga nenhuma:", response.status_code)
