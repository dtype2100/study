from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(256), nullable=False)
    # contents = Column(String(256), primary_key=True, nullable=False)
    is_done = Column(Boolean, nullable=False)


    def __repr__(self):
        return f"Todo (id={self.id}, contents={self.contents}, is_done={self.is_done})"