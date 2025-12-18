import time
import random


def run_benchmark() -> dict:
    time.sleep(random.uniform(0.2, 0.6))
    return {
        "tokens_per_second": random.randint(8, 30),
        "latency_ms": random.randint(80, 300)
    }
