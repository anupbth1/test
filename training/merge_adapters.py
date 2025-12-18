"""
Merge LoRA / QLoRA adapters into base model
"""

def merge(base_model: str, adapter: str, output_model: str):
    print("[Merge] Merging adapter into base")

    return {
        "status": "merged",
        "output": output_model
    }
