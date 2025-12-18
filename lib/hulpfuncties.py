############# Hulpfuncties om de input makkelijker te lezen #############
# Je kunt deze functies importeren in je eigen code
# door `import hulpfuncties` bovenaan je code te schrijven
#
# Wil je zelf een hulpfunctie toevoegen? Geen probleem!
# voeg gewoon de functie hieronder toe, sla de wijziginge op,
# en het werkt.

from pathlib import Path

def lees_bestand(directory, bestandsnaam) -> str:
    """Geeft de inhoud van een tekstbestand als string.
    Het bestand moet in dezelfde map staan als het JavaScript-bestand
    dat deze functie aanroept.

    Args:
        directory (str): de map waarin het bestand staat. Vul hier altijd __dirname in.
        bestandsnaam (str): de naam van de file, zoals "input.txt".

    Returns:
        str: tekstbestand als string
    """
    path = Path(directory) / bestandsnaam
    text = path.read_text().strip();
    if text == "":
        print(f"LET OP! {bestandsnaam} in de map {directory} is een leeg bestand")
    return text


def tekst_naar_regels(input_str) -> list[str]:
    """Converteert de Advent of Code input naar een array met iedere
    regel als afzonderlijk string element. Bijv.
    ```
    inputRegels = tekst_naar_regels(input);
    eersteRegel = inputRegels[0];
        ```

    Args:
        input_str(str): de inputfile van advent of code

    Returns:
        list[str]: een lijst met regels als string
    """
    return input_str.strip().splitlines()


def tekst_naar_getallen(input_str) -> list[int]:
    """Converteert de Advent of Code input die bestaat uit een lijst van getallen
    naar een lijst met die afzonderlijke getallen.

    Args:
        input_str(str): de inputfile van advent of code

    Returns:
        list[int]: een lijst met getallen
    """

    return [int(x) for x in input_str.strip().splitlines()]


def regel_naar_woorden(regel) -> list[str]:
    """Converteert een string van één regel naar een array met de
    losse woorden van die regel.
    
    Args:
        regel (str): de string waarvan je de losse woorden wilt
        
    Returns:
        list[str]: een lijst met alle losse woorden
    """
    return regel.strip().split()