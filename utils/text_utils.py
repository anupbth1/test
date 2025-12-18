def truncate(text: str, max_len: int = 500) -> str:
    if text is None:
        return ""
    return text[:max_len] + ("..." if len(text) > max_len else "")


def normalize(text: str) -> str:
    return " ".join(text.strip().split())
