from __future__ import annotations

import orjson
from tqdm import tqdm
from typing import Callable, Any
from zstandard import ZstdDecompressor


class ZSTJSONL:
    def __init__(self, path: str, size: int = 1 << 20) -> None:
        self.stream = ZstdDecompressor(max_window_size=int(2**31)).stream_reader(
            open(path, "rb")
        )
        self.size = size
        self.buffer = b""
        self.lines = []

    def __iter__(self) -> dict:
        while True:
            try:
                yield next(self)
            except StopIteration:
                break

    def __next__(self) -> dict:
        if len(self.lines):
            return orjson.loads(self.lines.pop(0))
        else:
            chunk = self.stream.read(self.size)
            if chunk:
                self.lines = (self.buffer + chunk).split(b"\n")
                self.buffer = self.lines[-1]
                self.lines = self.lines[:-1]
                return orjson.loads(self.lines.pop(0))
            else:
                raise StopIteration()

    def process(self, handler: Callable = lambda x: x, n: int = None) -> list[Any]:
        data = list()
        count = 0
        for line in tqdm(self):
            data.append(handler(line))
            count += 1
            if n:
                if count == n:
                    break
        return data

    def ingest(self, handler: Callable = lambda x: x, n: int = None) -> None:
        for line in tqdm(self):
            count = 0
            for line in tqdm(self):
                handler(line)
                count += 1
                if n:
                    if count == n:
                        break
