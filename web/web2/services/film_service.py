from database import get_session, Film
from models import FilmCreateRequestDto, FilmResponseDto


class FilmService:
    @staticmethod
    def create_film(film_dto: FilmCreateRequestDto) -> FilmResponseDto:
        session = get_session()
        new_db_film = Film(**film_dto.model_dump())
        session.add(new_db_film)
        session.commit()
        new_film_dto = FilmResponseDto(id=new_db_film.id, **film_dto.model_dump())
        session.close()
        return new_film_dto
