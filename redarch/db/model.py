from pathlib import Path
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
    info: str = Field(
        index=True,
        description="Dynamic combination of 'title', 'title_header', 'description', 'public_description'.",
    )
    lang: Optional[str] = Field(
        index=True,
        default=None,
        description="ISO 639 Set 1 two letter language code.",
    )
    nsfw: Optional[bool] = Field(
        index=True,
        default=None,
        description="Whether the subreddit is 'not safe for work'.",
    )

    @property
    def url(self) -> str:
        """
        Link to main subreddit page, defaults to old reddit.
        """
        return f"https://old.reddit.com/r/{self.name}"

    @property
    def api(self) -> str:
        """
        Link to reddit API with full and up to date information.
        """
        return f"https://www.reddit.com/api/info.json?id={self.guid}"


class Submission(SQLModel, table=True): ...


class User(SQLModel, table=True): ...


class Comment(SQLModel, table=True): ...


def session(database: str | Path, echo: bool = False) -> Session:
    engine = create_engine(str(database), echo=echo)
    return Session(engine)


def create(database: str | Path, echo: bool = True) -> None:
    engine = create_engine(str(database), echo=echo)
    SQLModel.metadata.create_all(engine)
