from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class FilmActor(Base):
    __tablename__ = "FilmActor"

    film_id = Column(ForeignKey("Film.id"), primary_key=True)
    actor_id = Column(ForeignKey("Actor.id"), primary_key=True)

    film = relationship("Film", back_populates="film_actors")
    actor = relationship("Actor", back_populates="actor_films")

    def __str__(self):
        return f"FilmActor: Film({self.film_id}) Actor({self.actor_id})"

    def __repr__(self):
        return str(self)

