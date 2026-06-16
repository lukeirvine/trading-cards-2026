from typing import Protocol, Union

class FileSystemEvent:
    src_path: Union[str, bytes]
    is_directory: bool

class FileSystemEventHandler(Protocol):
    def on_any_event(self, event: FileSystemEvent) -> None: ...
