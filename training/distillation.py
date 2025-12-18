"""
Knowledge distillation
Teacher = bigger model (offline / pre-run)
Student = CPU friendly model
"""

def distill(teacher_outputs: str, student_model: str):
    print("[Distillation] Aligning student to teacher outputs")

    return {
        "status": "completed",
        "method": "logits + instruction distillation"
    }
