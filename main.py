from typing import Union
from datetime import datetime
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health():
    return {"healthy": "up", "http_status": 200}

@app.get("/items/{item_id}")
async def read_item(item_id: int, user_agent: Union[str, None] = Header(default=None), Connection: Union[str, None] = Header(default=None)):
    now = datetime.now()
    f = open("/data/items.txt", "a")
    f.write("{\"Item Num\": \"" + str(item_id) + "\", \"date\": \"" + str(now) + "\", \"User-Agent\": \"" + user_agent + "\"}\n")
    return {"item_id": item_id, "Headers": {"Connection": Connection, "User-Agent": user_agent}}
