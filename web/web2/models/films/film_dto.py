from pydantic import BaseModel


class FilmCreateRequestDto(BaseModel):
    title: str
    duration: int | None = None
    category_id: int


class FilmResponseDto(FilmCreateRequestDto):
    id: int