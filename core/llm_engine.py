class LLMEngine:
    def __init__(self):
        self.current_quant = "Q4_K_M"

    def load_model(self, quant: str):
        self.current_quant = quant
        print(f"[LLM] Loaded model with quantization: {quant}")

    def generate(self, prompt: str) -> str:
        return (
            f"[LLM OUTPUT | Quant={self.current_quant}]\n"
            f"{prompt[:400]}"
        )
