"""
CPU-friendly LoRA fine-tuning (lightweight)
"""

def train_lora(base_model: str, dataset: str, output_dir: str):
    print("[LoRA] Starting training")
    print(f"Base model: {base_model}")
    print(f"Dataset: {dataset}")
    print("Using small rank, few epochs (CPU safe)")

    # placeholder for actual LoRA logic
    result = {
        "status": "completed",
        "adapter": output_dir + "/lora_adapter.bin",
        "epochs": 2,
        "rank": 8
    }

    return result
