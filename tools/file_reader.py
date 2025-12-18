from pathlib import Path

MAX_MB = 50


def read_file(path: str) -> str:
    p = Path(path)
    if not p.exists() or not p.is_file():
        raise FileNotFoundError(path)

    size_mb = p.stat().st_size / (1024 * 1024)
    if size_mb > MAX_MB:
        raise ValueError("File too large")

    return p.read_text(encoding="utf-8", errors="ignore")
