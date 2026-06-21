peak_intensities = [
    12.4,
    13.1,
    11.8,
    14.0,
    13.7,
    12.9,
    13.3
]

def calculate_mean(peak_intensities):
    total = sum(peak_intensities)
    count = len(peak_intensities)
    mean = total / count
    return mean

def calculate_max(peak_intensities):
    max_intensity = max(peak_intensities)
    return max_intensity

def calculate_min(peak_intensities):
    min_intensity = min(peak_intensities)
    return(min_intensity)

summary_table = {
    "Mean": calculate_mean(peak_intensities),
    "Max": calculate_max(peak_intensities),
    "Min": calculate_min(peak_intensities)
}

print("Spectral Summary Table:")
print("-----------------------")
print(f"Number of Peaks: {len(peak_intensities)}")
print(f"Mean Intensity: {summary_table['Mean']:.1f}")
print(f"Minimum Intensity: {summary_table['Min']:.2f}")
print(f"Maximum Intensity: {summary_table['Max']:.3f}")
