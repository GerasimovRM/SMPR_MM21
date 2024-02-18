from sqlalchemy import Column, Integer, String

from .base_meta import Base


class Category(Base):
    __tablename__ = "Category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)

    def __str__(self):
        return f"Category {self.id} {self.title}"
