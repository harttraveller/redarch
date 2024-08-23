from typing import Optional
from sqlmodel import SQLModel, Session, Field, create_engine


class Subreddit(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        description="Primary database key used by SQLite.",
    )


class Submission(SQLModel, table=True): ...


class User(SQLModel, table=True): ...


class Comment(SQLModel, table=True): ...
