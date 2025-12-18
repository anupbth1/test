"""
Quantization experiments (search space)
"""

SUPPORTED = ["Q6_K", "Q5_K_M", "Q4_K_M", "Q3_K_M"]

def quantize(model_path: str, scheme: str):
    if scheme not in SUPPORTED:
        raise ValueError("Unsupported quantization")

    print(f"[Quant] Applying {scheme}")

    return {
        "status": "completed",
        "scheme": scheme
    }
