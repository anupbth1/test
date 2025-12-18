class ReflectorAgent:
    def reflect(self, history: list):
        if not history:
            return {"lesson": "No data yet"}

        last = history[-1]
        return {
            "lesson": f"Task {last['task']['type']} scored {last['score']}",
            "action": "Adjust next plan slightly"
        }
