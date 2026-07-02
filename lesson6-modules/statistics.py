def average(signals):
    if not isinstance(signals, list) or len(signals) == 0:
        return None
    return sum(signals) / len(signals)


def minimum(signals):
    if not isinstance(signals, list) or len(signals) == 0:
        return None
    return min(signals)


def maximum(signals):
    if not isinstance(signals, list) or len(signals) == 0:
        return None
    return max(signals)