import time
import threading

from core.controller import Controller
from core.scheduler import Scheduler
from core.state_manager import StateManager
from core.error_handler import ErrorHandler

from agents.coordinator import CoordinatorAgent

from utils.time_utils import sleep_safe
from utils.path_utils import ensure_dir


def main():
    print("[MAIN] AI_RESEARCHER starting...")

    # Ensure runtime directories exist
    ensure_dir("logs")
    ensure_dir("research/experiments/results")

    # Core system objects
    state_manager = StateManager()
    memory = {}  # temporary shared memory object (can be replaced later)

    scheduler = Scheduler()
    controller = Controller(state_manager)

    coordinator = CoordinatorAgent(
        state_manager=state_manager,
        memory=memory
    )

    errors = ErrorHandler()

    print("[MAIN] System initialized")

    # Main autonomous loop
    while True:
        try:
            if state_manager.is_active():
                print("[MAIN] Research cycle running")

                # 1️⃣ Planning
                plan = coordinator.plan()

                # 2️⃣ Research
                ideas = coordinator.research(plan)

                # 3️⃣ Experimentation
                results = coordinator.experiment(ideas)

                # 4️⃣ Evaluation
                score = coordinator.evaluate(results)

                # 5️⃣ Critique & Reflection
                coordinator.reflect(score)

                # Update system state
                state_manager.update_last_result(score)

                # Cooldown between cycles
                scheduler.cooldown()

            else:
                print("[MAIN] Idle – waiting for activation")

            sleep_safe(5)

        except Exception as e:
            errors.handle(e)
            sleep_safe(10)


if __name__ == "__main__":
    main()
