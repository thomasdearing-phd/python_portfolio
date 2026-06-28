samples = [
    {"id": "STD001", "type": "STD", "signal": 125.2},
    {"id": "STD002", "type": "STD", "signal": 249.4},
    {"id": "QC001", "type": "QC", "signal": 311.2},
    {"id": "UNK001", "type": "UNK", "signal": 198.6},
    {"id": "UNK002", "type": "UNK", "signal": -2.4},
    {"id": "QC002", "type": "QC", "signal": 305.1},
]

num_stds = 0
num_qcs = 0
num_inks = 0

total_samples = len(samples)

for sample in samples:
    if sample['type'] == 'STD':
        num_stds += 1
    elif sample['type'] == 'QC':
        num_qcs += 1
    elif sample['type'] == 'UNK':
        num_inks += 1

valids = 0
invalids = 0

for samples in samples:
    if sample['signal'] < 0:
        sample['signal_status'] = 'FAIL'
        invalids += 1
    elif sample['signal'] >= 0:
        sample['signal_status'] = 'PASS'
        valids += 1

average_signal = sum(sample["signal"] for sample in samples) / len(samples)
highest_signal = max(sample["signal"] for sample in samples)
lowest_signal = min(sample["signal"] for sample in samples)

types = list(set(sample['type'] for sample in samples))

operators = [
    "Tom",
    "Alice",
    "Tom",
    "Bob",
    "Alice",
    "Emma"
]

ids = []

for sample in samples:
    ids.append(sample['id'])

print("Laboratory Summary")
print("------------------")
print(f'Total Samples: {total_samples}')
print(f'Number of STDs: {num_stds}')
print(f'Number of QCs: {num_qcs}')
print(f'Number of UNKs: {num_inks}')
print(f'Average Signal: {average_signal}')
print(f'Highest Signal: {highest_signal}')
print(f'Lowest Signal: {lowest_signal}')
print(f'Types of Samples: {types}')
print(f'Valid Samples: {valids}')
print(f'Invalid Samples: {invalids}')
print(f'Operators: {set(operators)}')
print(f'Sample IDs: {sorted(ids)}')

