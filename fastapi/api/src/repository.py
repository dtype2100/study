from sqlalchemy import select
from sqlalchemy.orm import Session
from database.orm import Todo
from typing import List

def get_todos(session: Session) -> List[Todo]:
    return list(session.scalars(select(Todo)))