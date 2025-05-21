from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.put('/items/{item_id}')
def update_item(item_id, item: Item):
    return {'item_name' : item.name, 'item_price': item.price}