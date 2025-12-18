import traceback
from utils.time_utils import now_str


class ErrorHandler:
    def __init__(self, log_file: str = "logs/errors.log"):
        self.log_file = log_file

    def handle(self, error: Exception):
        msg = f"[{now_str()}] ERROR {type(error).__name__}: {error}\n"
        trace = traceback.format_exc()

        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(msg)
            f.write(trace)
            f.write("\n")

        print(msg)
