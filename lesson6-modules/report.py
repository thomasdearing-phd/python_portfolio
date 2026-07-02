def print_header():
    print("Laboratory Summary")
    print("------------------")


def print_summary(num_stds, num_qcs, num_unks, valid_signals, invalid_signals):
    print(f"Total Samples:   {len(valid_signals) + len(invalid_signals)}")
    print(f"Number of STDs:  {num_stds}")
    print(f"Number of QCs:   {num_qcs}")
    print(f"Number of UNKs:  {num_unks}")

    print()

    print(f"Valid Signals:   {len(valid_signals)}")
    print(f"Invalid Signals: {len(invalid_signals)}")