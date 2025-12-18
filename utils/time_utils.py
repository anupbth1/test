import time
from datetime import datetime


def now_str() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def sleep_safe(seconds: int):
    time.sleep(max(0, seconds))
