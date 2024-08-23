from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Session, Field, create_engine


class Subreddit(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        description="Primary database key used by SQLite.",
    )
    created: datetime = Field(
        index=True,
        description="Subreddit creation timestamp.",
    )
    guid: str = Field(
        index=True,
        unique=True,
        description="Globally unique subreddit ID, eg: 't5_6'.",
    )
    name: str = Field(
        unique=True,
        index=True,
        description="Natural name of the subreddit, eg: 'news'.",
    )


class Submission(SQLModel, table=True): ...


class User(SQLModel, table=True): ...


class Comment(SQLModel, table=True): ...
