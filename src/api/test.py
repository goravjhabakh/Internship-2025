import time
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get('/1')
async def endpoint1():
    print('Hello')
    await asyncio.sleep(5)
    print('World')