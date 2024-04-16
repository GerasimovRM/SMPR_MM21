import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from database import Film

app = FastAPI()


class User(BaseModel):
    fio: str
    bdate: str | None = None


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    user: User


class FilmDto(BaseModel):
    id: int
    title: str
    duration: int | None = None
    category_id: int


@app.get("/")
async def root():
    return {"message": "Hello World",
            "body": [{"key": "value"}]}


@app.post("/")
async def root():
    return {"message2345": "Hello3456 World3456",
            "body3456": [{"key3456": "value3456"}]}


@app.get("/user/{username}")
async def read_item(username):
    return {"user": username}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return skip, limit


@app.post("/items/")
async def create_item(item: Item):
    return item



if __name__ == "__main__":
    uvicorn.run("main:app", port=5500, reload=True)
