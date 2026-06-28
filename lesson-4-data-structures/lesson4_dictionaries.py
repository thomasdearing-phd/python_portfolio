## Exercise 5

instrument = {
    "model": "...",
    "laser": 785,
    "detector": "...",
    "resolution": 4
}

for key, value in instrument.items():
    print(f'{key}: {value}')

##Exercise 6

samples = [

    {
        "sample_id":"QC001",
        "signal":123.4,
        "status":"PASS"
    },

    {
        "sample_id":"QC002",
        "signal":119.8,
        "status":"PASS"
    }

]

average_signal = sum(sample["signal"] for sample in samples) / len(samples)
highest_signal = max(sample["signal"] for sample in samples)
lowest_signal = min(sample["signal"] for sample in samples)
num_pass_samples = sum(1 for sample in samples if sample["status"] == "PASS")
num_fail_samples = len(samples) - num_pass_samples

print(f'Average signal: {average_signal}')
print(f'Highest signal: {highest_signal}')
print(f'Lowest signal: {lowest_signal}')
print(f'Number of PASS samples: {num_pass_samples}')
print(f'Number of FAIL samples: {num_fail_samples}')
