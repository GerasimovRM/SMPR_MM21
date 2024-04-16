from typing import List

from fastapi import HTTPException
from starlette import status

from database import get_session, Film
from models import FilmCreateRequestDto, FilmResponseDto, FilmPutRequestDto


class FilmService:
    @staticmethod
    def create_film(film_dto: FilmCreateRequestDto) -> FilmResponseDto:
        session = get_session()
        new_db_film = Film(**film_dto.model_dump())
        session.add(new_db_film)
        session.commit()
        new_film_dto = FilmResponseDto(**new_db_film.to_dict())
        session.close()
        return new_film_dto

    @staticmethod
    def get_all() -> List[FilmResponseDto]:
        session = get_session()
        db_films = session.query(Film).all()
        dto_films = list(map(lambda film: FilmResponseDto(**film.to_dict()), db_films))
        session.close()
        return dto_films

    @staticmethod
    def get_by_id(film_id: int) -> FilmResponseDto:
        session = get_session()
        db_film = session.query(Film).get(film_id)
        if not db_film:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Film with id {film_id} not found")
        return FilmResponseDto(**db_film.to_dict())

    @staticmethod
    def delete_by_id(film_id: int) -> FilmResponseDto:
        session = get_session()
        db_film = session.query(Film).get(film_id)
        if not db_film:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Film with id {film_id} not found")
        session.delete(db_film)
        session.commit()
        return FilmResponseDto(**db_film.to_dict())

    @staticmethod
    def put_by_id(film_id: int, film_date: FilmPutRequestDto) -> FilmResponseDto:
        session = get_session()
        db_film = session.query(Film).get(film_id)
        if not db_film:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Film with id {film_id} not found")
        db_film.update_from_pydantic(film_date)
        session.commit()
        return FilmResponseDto(**db_film.to_dict())
