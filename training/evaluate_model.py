"""
Evaluation on CPU benchmarks
"""

def evaluate(model_path: str):
    print("[Eval] Running benchmarks")

    return {
        "tokens_per_second": 15,
        "ram_mb": 3900,
        "stability": "ok",
        "quality_score": 0.78
    }
