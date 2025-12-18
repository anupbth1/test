import requests

TIMEOUT = 10


def fetch_text(url: str) -> str:
    r = requests.get(url, timeout=TIMEOUT)
    r.raise_for_status()
    return r.text[:100_000]  # hard cap
