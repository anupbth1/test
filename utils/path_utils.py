from pathlib import Path


def ensure_dir(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)


def resolve(path: str) -> str:
    return str(Path(path).expanduser().resolve())
