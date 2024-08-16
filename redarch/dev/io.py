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
        handler: Callable[[dict[str, Any]], Any] = lambda x: x,
        progress: bool = True,
        stop: Optional[int] = None,
    ) -> list[Any]:
        """
        Read in objects line by line.

        Args:
            handler (Callable[[dict[str, Any], Any]]): Custom Handler or parser for each object.
            progress (bool): Whether to show the progress with tqdm. Defaults to True.
            stop (int, Optional): Line to stop at. If None, continues until end of file. Defaults to None.

        Returns:
            list[Any]: Array of parsed objects.
        """
        data = list()
        count = 0
        for line in tqdm(self, disable=not progress):
            data.append(handler(line))
            count += 1
            if stop:
                if count == stop:
                    break
        return data
