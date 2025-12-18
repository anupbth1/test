class EfficiencyAgent:
    def select_quant_profile(self, metrics: dict):
        tps = metrics.get("tokens_per_second", 0)
        ram = metrics.get("ram_mb", 99999)

        # Simple but effective policy
        if ram > 8000:
            return "Q3_K_M"
        if tps < 10:
            return "Q5_K_M"
        return "Q4_K_M"

    def analyze(self, metrics: dict):
        efficiency = round(
            metrics.get("tokens_per_second", 0) /
            max(metrics.get("ram_mb", 1), 1),
            4
        )

        return {
            "efficiency_score": efficiency,
            "recommended_quant": self.select_quant_profile(metrics)
        }
