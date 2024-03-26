from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base_meta import Base


class Category(Base):
    __tablename__ = "Category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    films = relationship("Film", back_populates="category")

    def __str__(self):
        return f"Category {self.id} {self.title}"

    def __repr__(self):
        return str(self)