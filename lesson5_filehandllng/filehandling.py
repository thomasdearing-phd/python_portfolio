with open("students.txt") as file:

    for line in file:

        student = line.strip()

        print(f"Student : {student}")

data = []
with open('numbers.txt') as file:
    for line in file:
        number = float(line.strip())
        data.append(number)

total = sum(data)
print(f"Total: {total}")
max_number = max(data)
print(f"Max: {max_number}")
min_number = min(data)
print(f"Min: {min_number}")
average = total / len(data)
print(f"Average: {average}")


import csv

num_stds = 0
num_qcs = 0
num_inks = 0

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
            num_inks += 1
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
print(f'Number of UNKs: {num_inks}')
print(f'                     ')
print(f'Valid Signals: {len(valid_signals)}')
print(f'Invalid Signals: {len(invalid_signals)}')
print(f'                     ')
print(f'Average Valid Signal: {average_valid:.2f}')

report = [{
    "total_samples": len(valid_signals) + len(invalid_signals),
    "num_stds": num_stds,
    "num_qcs": num_qcs,
    "num_inks": num_inks,
    "valid_signals": len(valid_signals),
    "invalid_signals": len(invalid_signals),
    "average_valid_signal": average_valid
}]

with open("results.csv", "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=report[0].keys()
    )

    writer.writeheader()

    writer.writerows(report)