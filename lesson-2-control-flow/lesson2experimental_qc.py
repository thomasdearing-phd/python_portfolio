samples = [
    {"sample_id": "STD_001", "concentration": 10.0, "signal": 125.2},
    {"sample_id": "STD_002", "concentration": 20.0, "signal": 248.7},
    {"sample_id": "STD_003", "concentration": 30.0, "signal": 371.5},
    {"sample_id": "UNK_001", "concentration": None, "signal": 190.4},
    {"sample_id": "UNK_002", "concentration": None, "signal": -5.0},
    {"sample_id": "QC_001", "concentration": 25.0, "signal": 310.1},
]
def validate_signal(signal):
    if signal < 0:
        return "invalid"
    elif signal > 500:
        return "high"
    else:
        return "valid"
    
def calculate_response_factor(concentration, signal):
    if concentration is None:
        return None
    elif concentration <= 0:
        return None
    else:
        return signal / concentration
    
def sample_type(sample_id):
    if sample_id.startswith("STD"):
        return "standard"
    elif sample_id.startswith("UNK"):
        return "unknown"
    elif sample_id.startswith("QC"):
        return "quality_control"
    else:
        return "unknown_type"
    

for sample in samples:
    sample['signal_status'] = validate_signal(sample['signal'])
    sample['response_factor'] = calculate_response_factor(sample['concentration'], sample['signal'])
    sample['sample_type'] = sample_type(sample['sample_id'])

statuses = list()
for sample in samples:
    statuses.append(sample['signal_status'])




    

print(f"Experimental Report")
print(f"--------------------")
print(f"Total Samples: {len(samples)}"),
print(f"Valid_Signals: {statuses.count('valid')}"),
print(f"Invalid_Signals: {statuses.count('invalid')}"),
print(f"High_Signals: {statuses.count('high')}")
print(" " )

for sample in samples:
    print(f"Sample ID: {sample['sample_id']}, Signal Status: {sample['signal_status']}, Response Factor: {sample['response_factor']}, Sample Type: {sample['sample_type']}")