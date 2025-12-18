try:
    import psutil
except ImportError:
    psutil = None


def cpu_usage_percent() -> float:
    if psutil is None:
        return -1.0
    return psutil.cpu_percent(interval=0.5)
