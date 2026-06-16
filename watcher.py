import subprocess
import sys
import time
from threading import Timer

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, script_to_run: str, ignore_folder: str) -> None:
        self.script_to_run = script_to_run
        self.timer = Timer(0, lambda: None)
        self.debounce_delay = 1  # seconds
        self.ignore_folder = ignore_folder

    def on_any_event(self, event: FileSystemEvent) -> None:
        raw_path = event.src_path
        if isinstance(raw_path, bytes):
            src_path = raw_path.decode("utf-8")
        else:
            src_path = str(raw_path)
        # Ignore directories, temporary files, and files in the ignore folder
        if event.is_directory or src_path.endswith(("~", ".swp", ".tmp")) or self.ignore_folder in src_path:
            return
        print(f"{src_path} has been modified. Debouncing...")
        if self.timer:
            self.timer.cancel()
        self.timer = Timer(self.debounce_delay, self.run_script)
        self.timer.start()

    def run_script(self) -> None:
        print(f"Running {self.script_to_run}...")
        subprocess.call([sys.executable, self.script_to_run, "--from-watcher"])


if __name__ == "__main__":
    path = "."  # The directory to watch
    script_to_run = "src/trading_cards/main.py"  # The script to run when a file changes
    ignore_folder = "output"  # Folder to ignore

    event_handler = ChangeHandler(script_to_run, ignore_folder)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print(f"Watching for changes in {path}, ignoring {ignore_folder}...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
