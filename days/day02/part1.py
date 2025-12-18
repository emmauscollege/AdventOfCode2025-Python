import os
import hulpfuncties

# Lees input.txt uit dezelfde map als dit bestand
input = hulpfuncties.lees_bestand(os.path.dirname(__file__), "input.txt")

alle_ranges = input.split(",")

for range in alle_ranges:
    min_max_list = range.split("-")
    range_minimum = min_max_list[0]
    range_maximum = min_max_list[1]

    print(f"Range: minimum is {range_minimum} en het maximum is {range_maximum}")