from fastapi import FastAPI

from api.controller import film_controller

app = FastAPI()
app.include_router(film_controller)