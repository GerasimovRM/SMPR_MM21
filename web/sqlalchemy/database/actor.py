from datetime import date

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from .base_meta import Base


class Actor(Base):
    __tablename__ = "Actor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    middle_name = Column(String(100), nullable=True)
    bdate = Column(Date, nullable=False)

    actor_films = relationship("FilmActor", back_populates="actor")

    def __str__(self):
        return f"Actor {self.id} {self.first_name} {self.last_name} {self.middle_name if self.middle_name else ''}"

    def __repr__(self):
        return str(self)

