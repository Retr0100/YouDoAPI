from sqlmodel import Relationship, SQLModel, Field

from model.user import User
class Todo(SQLModel, table=True):
    """This is a the model for the table in the DB.

    Args:
        SQLModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """
    __tablename__ = "dailyTodo"

    id: int | None = Field(None,primary_key=True,nullable=True)
    title: str
    description:str | None
    date_created:str
    date_expire:str
    status_done:bool
    priority:int
    favorite:bool
    user_id: int = Field(foreign_key="users.id")
    user: "User" = Relationship(back_populates="todos")


