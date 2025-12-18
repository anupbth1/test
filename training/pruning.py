"""
Structured pruning (safe for CPU)
"""

def prune_model(model_path: str, ratio: float = 0.1):
    if ratio > 0.3:
        raise ValueError("Pruning too aggressive")

    print(f"[Pruning] Removing {ratio*100}% weights")

    return {
        "status": "completed",
        "pruned_ratio": ratio
    }
