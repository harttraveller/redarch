from __future__ import annotations

import orjson
from tqdm import tqdm
from pathlib import Path
from typing import Callable, Generator, Optional, Any
from zstandard import ZstdDecompressor
from redarch import var


class ZSTJSONL:
    def __init__(
        self,
        path: str | Path,
        size: int = 1 << 20,
    ) -> None:
        """
        Interface for JSONL data in compressed ZST archive file.

        Args:
            path (str | Path): The path to the ZST file containing JSONL data.
            size (int, optional): The chunk size of loaded data in bytes. Defaults to 1<<20.
        """
        self.stream = ZstdDecompressor(
            max_window_size=var.ZST_MAX_WINDOW_SIZE_CONSTANT
        ).stream_reader(open(path, "rb"))
        self.size = size
        self.buffer = b""
        self.lines = []

    def __iter__(self) -> Generator[dict[str, Any], None, None]:
        while True:
            try:
                yield next(self)
            except StopIteration:
                break

    def __next__(self) -> dict[str, Any]:
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

    def read(
        self,
        parser: Callable[[dict[str, Any]], Any] = lambda x: x,
        progress: bool = True,
        stop: int = -1,
    ) -> list[Any]:
        """
        Read in objects line by line.

        Args:
            parser (Callable[[dict[str, Any], Any]]): Custom parser for each object.
            progress (bool): Whether to show the progress with tqdm. Defaults to True.
            stop (int): Line to stop at. If -1, continues until end of file. Defaults to -1.

        Returns:
            list[Any]: Array of parsed objects.
        """
        data: list[Any] = list()
        count: int = 0
        # todo.fix: if on each iter is slow
        for line in tqdm(self, disable=not progress, total=None if stop < 0 else stop):
            data.append(parser(line))
            if count == stop:
                break
            count += 1
        return data

    def ingest(
        self,
        handler: Callable[[dict[str, Any]], None] = lambda x: None,
        progress: bool = True,
        stop: int = -1,
    ) -> None:
        """
        Ingest objects, passing each one to a custom handler.

        Args:
            handler (Callable[[dict[str, Any], Any]]): Custom handler for each object.
            progress (bool): Whether to show the progress with tqdm. Defaults to True.
            stop (int): Line to stop at. If -1, continues until end of file. Defaults to -1.

        Returns:
            list[Any]: Array of parsed objects.
        """
        count: int = 0
        # todo.fix: if on each iter is slow
        for line in tqdm(self, disable=not progress, total=None if stop < 0 else stop):
            handler(line)
            if count == stop:
                break
            count += 1
