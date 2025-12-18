class CriticAgent:
    def critique(self, output: dict):
        issues = []
        if "error" in output:
            issues.append("Execution failed")
        if len(output) == 0:
            issues.append("No meaningful output")

        return {
            "issues": issues,
            "acceptable": len(issues) == 0
        }
