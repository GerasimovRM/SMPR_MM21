import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World",
            "body": [{"key": "value"}]}


@app.post("/")
async def root():
    return {"message2345": "Hello3456 World3456",
            "body3456": [{"key3456": "value3456"}]}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5500, reload=True)
