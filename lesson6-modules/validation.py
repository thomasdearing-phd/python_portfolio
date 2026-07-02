def validate_signal(signal):
    if signal >= 0:
        return "VALID"
    return "INVALID"

def validate_sample_type(sample_type):
    if sample_type in ("STD", "QC", "UNK"):
        return sample_type
    return None