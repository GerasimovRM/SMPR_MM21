import uvicorn
from fastapi import FastAPI
from models import FilmCreateRequestDto
from services import FilmService

app = FastAPI()


@app.post("/film/create")
def film_create(film: FilmCreateRequestDto):
    return FilmService.create_film(film)


if __name__ == "__main__":
    uvicorn.run("main:app", port=5500, reload=True)
