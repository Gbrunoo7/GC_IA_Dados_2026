from fastapi import FastAPI, HTTPException
import requests
import uvicorn

app = FastAPI(title="Fruits API", description="API para consultar informações de frutas")
fruits = [] # list in mem

def get_fruit_by_name(nome: str):
    nome = nome.lower()
    for fruit in fruits:
        if fruit['name'] == nome:
            return fruit

    resposta = requests.get(f"https://www.fruityvice.com/api/fruit/{nome.strip().lower()}", timeout=10)
    if resposta.status_code != 200:
        raise HTTPException(status_code=404, detail="Fruta não encontrada")
    resposta.raise_for_status()

    data = resposta.json()
    return {
        "name": data["name"],
        "id": data["id"],
        "order": data["order"],
        "genus": data["genus"],
        "carbohydrates": data["carbohydrates"],
        "protein": data["protein"],
        "fat": data["fat"],
        "calories": data["calories"],
        "sugar": data["sugar"],
    }

#GET
@app.get("/")
def home():
    return {"message": "API FastAPI Rodando!"}

#GET - listar todas as frutas
@app.get("/fruits")
def get_all_fruits(fruit): # Para armazenar as frutas consultadas na memória
    return fruits(fruit)

#GET - buscar uma fruta pelo nome
@app.get("/fruits/{nome}")
def get_fruit(nome: str):
    return get_fruit_by_name(nome)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)