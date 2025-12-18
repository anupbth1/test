import json
from datetime import datetime


class StateManager:
    def __init__(self):
        self.history = []

    def log(self, message: str):
        print(f"[STATE] {message}")

    def update(self, task, result, score):
        entry = {
            "time": datetime.utcnow().isoformat(),
            "task": task,
            "result": result,
            "score": score,
        }
        self.history.append(entry)

class StateManager:
    def __init__(self):
        self.active = True
        self.current_state = "INIT"

    def is_active(self) -> bool:
        return self.active

    def stop(self):
        self.active = False

    def set_state(self, state: str):
        self.current_state = state

    def get_state(self) -> str:
        return self.current_state
