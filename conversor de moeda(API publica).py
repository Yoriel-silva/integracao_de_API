import requests
import json

cotaçoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotaçoes = cotaçoes.json()
cotaçoes_dolar = cotaçoes['USDBRL']['bid']
print(cotaçoes_dolar)