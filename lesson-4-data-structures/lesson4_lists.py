signals = [
    124.5,
    127.2,
    123.9,
    126.1,
    125.8
]
## Exercise 1
max_signal = max(signals)
min_signal = min(signals)
num_signals = len(signals)
average_signal = sum(signals) / num_signals

print(f'Max Signal= {max_signal}')
print(f'Min Signal= {min_signal}')
print(f'Average Signal= {average_signal}')
print(f'Number of Measurements= {num_signals}')

##EXercise 2

signals.extend([214,2,124,6,98.4])
signals.remove(126.1)
print(signals)


## Exercise 3

spectra = [
    "scan1",
    "scan2",
    "scan3",
    "scan4",
    "scan5",
    "scan6"
]

first_three_scans = spectra[:3]
last_three_scans = spectra[-3:]
middle_two_scans = spectra[2:4]

print(f'First three scans: {first_three_scans}')
print(f'Last three scans: {last_three_scans}')
print(f'Middle two scans: {middle_two_scans}')

## Exercise 4

instrument = (
    "Raman",
    785,
    "Thermo Fisher"
)

print(f'Instrument: {instrument[0]}')
print(f'Wavelength: {instrument[1]} nm')
print(f'Manufacturer: {instrument[2]}')
