import csv

num_stds = 0
num_qcs = 0
num_unks = 0

valid_signals = []
invalid_signals = []

with open("samples.csv") as file:
    reader = csv.DictReader(file)

    for sample in reader:
        if sample['type'] == 'STD':
            num_stds += 1
        elif sample['type'] == 'QC':
            num_qcs += 1
        elif sample['type'] == 'UNK':
            num_unks += 1
        else:
            print(f"Unknown sample type: {sample['type']}")

        if float(sample['signal']) >= 0:
            sample['signal_status'] = 'VALID'
            valid_signals.append(float(sample['signal']))
        else:
            sample['signal_status'] = 'INVALID'
            invalid_signals.append(float(sample['signal']))

average_valid = sum(valid_signals) / len(valid_signals)

print("Laboratory Summary")
print("------------------")
print(f'Total Samples: {len(valid_signals) + len(invalid_signals)}')
print(f'Number of STDs: {num_stds}')
print(f'Number of QCs: {num_qcs}')
print(f'Number of UNKs: {num_unks}')
print(f'                     ')
print(f'Valid Signals: {len(valid_signals)}')
print(f'Invalid Signals: {len(invalid_signals)}')
print(f'                     ')
print(f'Average Valid Signal: {average_valid:.2f}')

report = [{
    "total_samples": len(valid_signals) + len(invalid_signals),
    "num_stds": num_stds,
    "num_qcs": num_qcs,
    "num_unks": num_unks,
    "valid_signals": len(valid_signals),
    "invalid_signals": len(invalid_signals),
    "average_valid_signal": average_valid
}]

with open("qc_report.txt", "w", newline="") as file:
    file.write("QC Report\n")
    file.write("-----------\n")
    file.write(f'Total Samples: {len(valid_signals) + len(invalid_signals)}\n')
    file.write(f'Number of STDs: {num_stds}\n')
    file.write(f'Number of QCs: {num_qcs}\n')
    file.write(f'Number of UNKs: {num_unks}\n') 
    file.write(f'Valid Signals: {len(valid_signals)}\n')
    file.write(f'Invalid Signals: {len(invalid_signals)}\n')
    file.write(f'Average Valid Signal: {average_valid:.2f}\n')