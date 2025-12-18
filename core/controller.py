from core.scheduler import Scheduler
from core.llm_engine import LLMEngine
from core.prompt_manager import PromptManager
from core.execution_manager import ExecutionManager
from core.evaluation_manager import EvaluationManager


class Controller:
    def __init__(self, state_manager):
        self.state = state_manager
        self.scheduler = Scheduler()
        self.llm = LLMEngine()
        self.prompts = PromptManager()
        self.executor = ExecutionManager()
        self.evaluator = EvaluationManager()


        self.idle_sleep_seconds = self.scheduler.min_idle_sleep

    def run_cycle(self):
        task = self.scheduler.next_task()

        if not task:
            self.state.log("No task scheduled. Idling.")
            return

        self.state.log(f"Running task: {task['type']}")

        prompt = self.prompts.build(task)
        response = self.llm.generate(prompt)

        metrics = {"tokens_per_second": 15, "ram_mb": 4000}
        decision = self.evaluator.evaluate(task, {"metrics": metrics})
        self.llm.load_model(decision.get("recommended_quant", "Q4_K_M"))
        result = self.executor.execute(task, response, self.llm.current_quant)
        score = self.evaluator.evaluate(task, result)

        self.state.update(task, result, score)
