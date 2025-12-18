import time

# shared lightweight state
_STATE = {
    "active": False,
    "current_goal": "CPU-efficient quantization",
    "last_update": None,
    "last_result": None
}


def status_response():
    return {
        "active": _STATE["active"],
        "goal": _STATE["current_goal"],
        "last_update": _STATE["last_update"],
        "last_result": _STATE["last_result"]
    }


def command_response(cmd: dict):
    action = cmd.get("action")

    if action == "start":
        _STATE["active"] = True
        _STATE["last_update"] = time.ctime()
        return {"ok": True, "msg": "Research started"}

    if action == "stop":
        _STATE["active"] = False
        return {"ok": True, "msg": "Research stopped"}

    if action == "set_goal":
        _STATE["current_goal"] = cmd.get("goal", _STATE["current_goal"])
        return {"ok": True, "msg": "Goal updated"}

    if action == "summarize":
        return {
            "summary": "Best result so far: Q4_K_M baseline, stable, CPU efficient"
        }

    return {"ok": False, "msg": "Unknown command"}


def research_state():
    return _STATE
