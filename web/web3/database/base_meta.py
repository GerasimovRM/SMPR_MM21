from pydantic import BaseModel
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DB_HOST, DB_PORT, DB_PASSWORD, DB_USER, DB_NAME

Base = declarative_base()
# print(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
get_session = sessionmaker(engine, autocommit=False)


class BaseSQlAlchemyModel(Base):
    __abstract__ = True

    def to_dict(self):
        return {column.key: getattr(self, column.key) for column in inspect(self).mapper.column_attrs}

    def update_from_pydantic(self, model: BaseModel):
        for key, value in model.model_dump(exclude_none=True).items():
            if hasattr(self, key):
                setattr(self, key, value)

