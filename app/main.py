from fastapi import FastAPI

app  = FastAPI()

@app.get("/")
def minha_api():
    return {"msg": "API rodando"}