class PromptManager:
    def build(self, task: dict) -> str:
        base = f"You are an AI researcher.\nTask type: {task['type']}\n"
        if task["type"] == "planning":
            return base + "Plan next research steps."
        if task["type"] == "research":
            return base + "Analyze latest efficiency techniques."
        if task["type"] == "experiment":
            return base + "Design a CPU-friendly experiment."
        if task["type"] == "evaluation":
            return base + "Evaluate experiment results."
        if task["type"] == "reflection":
            return base + "Reflect and improve future plans."
        return base
