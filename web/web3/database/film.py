from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import BaseSQlAlchemyModel


class Film(BaseSQlAlchemyModel):
    __tablename__ = "Film"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    duration = Column(Integer, nullable=True)
    category_id = Column(Integer, ForeignKey("Category.id"))

    category = relationship("Category", back_populates="films")
    film_actors = relationship("FilmActor", back_populates="film")

    def __str__(self):
        return f"Film {self.id} {self.title}"

    def __repr__(self):
        return str(self)

