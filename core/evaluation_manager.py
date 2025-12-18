class EvaluationManager:
    def evaluate(self, task, result):
        m = result["metrics"]

        efficiency_score = round(
            m["tokens_per_second"] / max(m["ram_mb"], 1),
            5
        )

        return {
            "efficiency": efficiency_score,
            "acceptable": efficiency_score > 0.002
        }
