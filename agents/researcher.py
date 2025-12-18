class ResearcherAgent:
    def __init__(self, memory):
        self.memory = memory

    def research(self, plan):
        """
        Takes a plan and produces research ideas / references
        """
        return {
            "topic": plan.get("goal", "CPU LLM efficiency"),
            "findings": [
                "Quantization reduces memory bandwidth pressure",
                "INT8/INT4 trade-offs on CPU",
                "KV-cache optimization improves throughput"
            ]
        }
