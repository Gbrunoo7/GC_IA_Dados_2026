from fastapi import FastAPI, HTTPException
import requests
import uvicorn

app = FastAPI(title="Pokédex API", description="API para consultar informações de Pokémon")
pokedex = [] # list in mem

def get_pokemon_by_name(nome: str):
    nome = nome.lower()
    for pokemon in pokedex:
        if pokemon['name'] == nome:
            return pokemon

    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome.strip().lower()}", timeout=10)
    if resposta.status_code != 200:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")
    resposta.raise_for_status()

    data = resposta.json()
    return {
        "name": data["name"],
        "id": data["id"],
    }

@app.get("/")
def home():
    return {"message": "API FastAPI Rodando!"}

@app.get("/pokemon")
def get_all_pokemon(pokemon): # Para armazenar os pokémons consultados na memória
    return pokedex(pokemon)

@app.get("/pokemon/{nome}")
def get_pokemon(nome: str):
    return get_pokemon_by_name(nome)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)