def efficiency_score(tokens_per_sec: float, ram_mb: float) -> float:
    if ram_mb <= 0:
        return 0.0
    return round(tokens_per_sec / ram_mb, 6)


def percent_change(old: float, new: float) -> float:
    if old == 0:
        return 0.0
    return round(((new - old) / old) * 100, 2)
