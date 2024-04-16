from typing import List

from fastapi import APIRouter, HTTPException, status

from models import FilmCreateRequestDto, FilmResponseDto
from models.films.film_dto import FilmPutRequestDto
from services import FilmService

controller = APIRouter(prefix="/film")


@controller.post("/", response_model=FilmResponseDto)
def film_create(film: FilmCreateRequestDto):
    return FilmService.create_film(film)


@controller.get("/", response_model=List[FilmResponseDto])
def get_all_films():
    return FilmService.get_all()


@controller.get("/{film_id}", response_model=FilmResponseDto | None)
def get_film_by_id(film_id: int):
    return FilmService.get_by_id(film_id)


@controller.put("/{film_id}", response_model=FilmResponseDto)
def put_film_by_id(film_id: int, film: FilmPutRequestDto):
    return FilmService.put_by_id(film_id, film)


@controller.delete("/{film_id}", response_model=FilmResponseDto)
def delete_film_by_id(film_id: int):
    return FilmService.delete_by_id(film_id)
