from msgspec import Struct


class Submission(Struct):
    is_self: bool
    created_utc: int | str
    selftext: str
    title: str
    score: int
    permalink: str
    over_18: bool
    num_comments: int
    id: str
    media_embed: dict
    edited: int | float | bool
    thumbnail: str
