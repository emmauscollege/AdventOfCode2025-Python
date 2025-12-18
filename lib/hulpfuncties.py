from pathlib import Path

def lees_bestand(directory, bestandsnaam):
    path = Path(directory) / bestandsnaam
    return path.read_text().strip()

def tekst_naar_regels(input_str):
    return input_str.strip().splitlines()

def tekst_naar_getallen(input_str):
    return [int(x) for x in input_str.strip().splitlines()]

def regel_naar_woorden(regel):
    return regel.strip().split()