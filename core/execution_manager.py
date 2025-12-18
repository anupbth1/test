import time
import random


class ExecutionManager:
    def execute(self, task, llm_response, quant="Q4_K_M"):
        start = time.time()

        # Simulated CPU-safe execution
        time.sleep(random.uniform(0.5, 1.2))

        tokens_per_second = random.randint(8, 25)
        ram_mb = random.randint(2000, 9000)

        return {
            "task": task["type"],
            "quant": quant,
            "output": llm_response[:200],
            "metrics": {
                "tokens_per_second": tokens_per_second,
                "ram_mb": ram_mb
            },
            "runtime": round(time.time() - start, 2)
        }
