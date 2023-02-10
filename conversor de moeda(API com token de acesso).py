import requests

moeda_base = str(input('Qual será a moeda base:'))
url = "https://api.apilayer.com/fixer/latest?base="+moeda_base 

payload = {}
headers= {
  "apikey": "acces_key"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)

y = str(input('Qual será a moeda de conversão: '))
x = result.find(y)

valor = float(input('Digite quanto de dinheiro deseja converter: '))
convercao = float(result[x + 6:x + 13]) * valor
print(convercao)
