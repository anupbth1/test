"""
Very simple local auth (optional)
Jarvis usually runs locally, so keep it minimal
"""

API_KEY = "local-dev-key"


def verify(key: str) -> bool:
    return key == API_KEY
