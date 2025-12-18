BLOCKED_KEYWORDS = [
    "rm -rf",
    "shutdown",
    "reboot",
    "mkfs",
    "dd if="
]


def is_safe(code: str) -> bool:
    lowered = code.lower()
    for k in BLOCKED_KEYWORDS:
        if k in lowered:
            return False
    return True
