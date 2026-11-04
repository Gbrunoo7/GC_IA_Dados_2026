import requests
import pprint
api_key = "YOUR_API_KEY"
base_url = "https://api.weatherapi.com/v1/"

link_api = base_url

parametros = {
    "key": api_key,
    "q": "London",
    "lang": "pt"
}

resposta = requests.get(f"{link_api}current.json", params=parametros)

print(resposta.status_code)
print(resposta.content)

if resposta.status_code == 200:
    dados = resposta.json()
    pprint.pprint(dados)
    temperatura = dados["current"]["temp_c"]
    print(temperatura)

'''
    ## current_weather_endpoint = "current.json"
    ## 
requests.get(base_url)
'''