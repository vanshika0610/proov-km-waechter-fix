# log_util.py
# A homemade logger.
# The standard logging module felt like "too much magic" in 2013.
# Style modernized 2024.

import time

LOG_LINES: list[str] = []       # global state, shared by everyone who imports this
DEBUG = False


def log(message: str) -> None:
    """Append a timestamped line to the in-memory log and print it."""
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {message}"
    LOG_LINES.append(line)
    print(line)


def debug(message: str) -> None:
    """Log a DEBUG-prefixed message — only active when DEBUG is True.

    DEBUG has been False since 2014; this branch is effectively dead code.
    """
    if DEBUG:
        log(f"DEBUG: {message}")


def flush_log(path: str) -> None:
    """Write all buffered log lines to the given file (append mode), then clear the buffer."""
    with open(path, "a") as f:
        for line in LOG_LINES:
            f.write(line + "\n")
    del LOG_LINES[:]
