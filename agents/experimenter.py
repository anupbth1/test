class ExperimenterAgent:
    def run(self, plan: dict):
        return {
            "experiment": "CPU quantized inference test",
            "parameters": {
                "quant": "Q4_K_M",
                "batch_size": 1
            }
        }
