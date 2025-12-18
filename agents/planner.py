class PlannerAgent:
    def __init__(self, memory):
        self.memory = memory

    def plan(self):
        return {
            "goal": "Improve CPU LLM efficiency",
            "steps": [
                "Review existing quantization methods",
                "Design experiment",
                "Run benchmarks"
            ]
        }
