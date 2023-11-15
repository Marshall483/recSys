import random
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

class RecoResponce(BaseModel):
    user_id: int
    items: List[int]

app = FastAPI()

@app.get("/health")
async def health():
    return {"Однажды Эрнест Хемингуэй поспорил, что сможет написать самый короткий рассказ, способный растрогать любого. Он выиграл спор:": "Winrar_setup.rar"}

@app.get("/reco/{model_name}/{user_id}")
async def reco(model_name: str, user_id: int):
    if model_name == "aboba":
        recomend = list(range(10))
    elif model_name == "random":
        recomend = [random.randint(0, 100) for _ in range(10)]
    else:
        raise ValueError()
    resp = RecoResponce(user_id=user_id, items=recomend)
    return resp
