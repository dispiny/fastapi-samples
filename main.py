from typing import Union
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def dumps():

    return {"healthy": "up", "http_status": 200}

@app.get("/items/{item_id}")
async def read_item(item_id: int, user_agent: Union[str, None] = Header(default=None), Connection: Union[str, None] = Header(default=None)):
    return {"item_id": item_id, "Headers": {"Connection": Connection, "User-Agent": user_agent}}