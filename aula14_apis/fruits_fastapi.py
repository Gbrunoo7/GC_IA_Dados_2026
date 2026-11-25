from fastapi import FastAPI, HTTPException
import requests
import uvicorn

# In progress

app = FastAPI(title="Fruits API", description="API para consultar informações de frutas")
fruits = [] # list in mem



def get_fruit_by_name(nome: str):
    nome = nome.lower().strip()
    for fruit in fruits:
        if fruit['name'] == nome:
            return fruit

    resposta = requests.get(f"https://www.fruityvice.com/api/fruit/{nome.strip().lower()}", timeout=10)
    if resposta.status_code != 200:
        raise HTTPException(status_code=404, detail="Fruta não encontrada")
    return resposta.json()

#GET
@app.get("/")
def home():
    return {"message": "API FastAPI Rodando!"}

#GET - listar todas as frutas
@app.get("/fruit/all")
def get_all_fruits():
    resposta = requests.get("https://www.fruityvice.com/api/fruit/all", timeout=10)
    if resposta.status_code != 200:
        raise HTTPException(status_code=404, detail="Não foi possível buscar as frutas")
    resposta.raise_for_status()

    return resposta.json()


#GET - buscar uma fruta pelo nome
@app.get("/fruit/{nome}")
def get_fruit(nome: str):
    return get_fruit_by_name(nome)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)