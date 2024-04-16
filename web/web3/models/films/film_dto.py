from pydantic import BaseModel


class FilmCreateRequestDto(BaseModel):
    title: str
    duration: int | None = None
    category_id: int


class FilmPutRequestDto(BaseModel):
    title: str | None = None
    duration: int | None = None
    category_id: int | None = None


class FilmResponseDto(FilmCreateRequestDto):
    id: int