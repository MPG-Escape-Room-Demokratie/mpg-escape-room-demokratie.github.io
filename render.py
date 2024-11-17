import glob
import json
import time
from dataclasses import dataclass
from typing import Any, Self

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent
from staticjinja import Site



if __name__ == "__main__":
    site = Site.make_site(
        mergecontexts=True,
    )

    site.render(use_reloader=True)
