signals = [125.2, 248.7, 371.5,331.76,971.45]
print(f"Number of Signals: {len(signals)}")
print(f"Max of Signals: {max(signals)}")
print(f"Min of Signals: {min(signals)}")
print(f"Average of Signals: {sum(signals) / len(signals):.2f}")

sample = {
    "Sample ID" : "QC_002",
    "Concentration" : 20,
    "Signal" : 255
}
## Excercise 3
sample['Status'] ="PASS"

samples = [
    {"sample_id": "STD_001", "signal": 125.2},
    {"sample_id": "STD_002", "signal": 248.7},
    {"sample_id": "STD_003", "signal": 371.5}
]

signals = []

for sample in samples:
    signals.append(sample['signal'])

mean = sum(signals) / len(signals)
print(f"Mean Signal: {mean:.2f}")

## Excercise 4
for sample in samples:
    if sample["signal"] > 200:
        print(sample)

## Excercise 5

samples = [
    {"sample_id": "STD_001", "concentration": 10.0, "signal": 125.2},
    {"sample_id": "STD_002", "concentration": 20.0, "signal": 248.7},
    {"sample_id": "STD_003", "concentration": 30.0, "signal": 371.5},
    {"sample_id": "UNK_001", "concentration": None, "signal": 190.4},
    {"sample_id": "UNK_002", "concentration": None, "signal": -5.0},
    {"sample_id": "QC_001", "concentration": 25.0, "signal": 310.1},
]

stds_count = len(samples)
print(f"SampleCount: {stds_count}")

std_samples = 0
qc_samples = 0
unk_samples = 0

for sample in samples:

    sample_id = sample["sample_id"]

    if sample_id.startswith("STD"):
        std_samples += 1

    elif sample_id.startswith("QC"):
        qc_samples += 1

    else:
        unk_samples += 1

print(f"Standard Samples: {std_samples}")
print(f"Quality Control Samples: {qc_samples}")
print(f"Unknown Samples: {unk_samples}")

## Excercise 6

samples = [
    {"sample_id": "STD_001", "concentration": 10.0, "signal": 125.2},
    {"sample_id": "STD_002", "concentration": 20.0, "signal": 248.7},
    {"sample_id": "STD_003", "concentration": 30.0, "signal": 371.5},
    {"sample_id": "UNK_001", "concentration": None, "signal": 190.4},
    {"sample_id": "UNK_002", "concentration": None, "signal": -5.0},
    {"sample_id": "QC_001", "concentration": 25.0, "signal": 310.1},
]

std_samples = 0
qc_samples = 0
unk_samples = 0

total_signal = 0

for sample in samples:

    sample_id = sample["sample_id"]

    if sample_id.startswith("STD"):
        std_samples += 1
        sample['type'] = 'Standard'

    elif sample_id.startswith("QC"):
        qc_samples += 1
        sample['type'] = 'Quality Control'

    elif sample_id.startswith("UNK"):
        unk_samples += 1
        sample['type'] = 'Unknown'
    else:
        print(f"Unrecognized Sample Type: {sample_id}")
        sample['type'] = 'Unrecognized'

    signal = sample['signal']
    total_signal += signal

    if signal <0:
        sample['validation'] = 'INVALID'

    elif signal > 500:
        sample['validation'] = 'HIGH'

    else:
        sample['validation'] = 'VALID'

average_signal = total_signal / len(samples)


