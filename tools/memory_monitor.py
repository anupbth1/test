try:
    import psutil
except ImportError:
    psutil = None


def ram_usage_mb() -> int:
    if psutil is None:
        return -1
    mem = psutil.virtual_memory()
    return int(mem.used / (1024 * 1024))
