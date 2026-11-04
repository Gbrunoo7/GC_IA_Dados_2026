import requests

def fetch_data(endpoint, filters={}):
    url = f"https://rickandmortyapi.com/api/{endpoint}"
    response = requests.get(url, params=filters)

    return response.json() if response.status_code == 200 else None

characters = fetch_data("character", {'name': 'Rick Sanchez'})

if characters and characters.get("results"):
    print(f"Total de personagens encontrados: {characters.get('info', {}).get('count', len(characters['results']))}\n")

    for character in characters["results"]:
        print("-" * 40)
        print(f"Nome: {character.get('name', 'N/A')}")
        print(f"Status: {character.get('status', 'N/A')}")
        print(f"Espécie: {character.get('species', 'N/A')}")
        print(f"Gênero: {character.get('gender', 'N/A')}")
        print(f"Origem: {character.get('origin', {}).get('name', 'N/A')}")
        print(f"Localização: {character.get('location', {}).get('name', 'N/A')}")
    print("-" * 40)
else:
    print("Nenhum dado retornado da API.")