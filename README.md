# Advent Of Code 2025 - python

Dit repository bevat een template om gemakkelijk in Python met de puzzels van [Advent of Code 2025](https://adventofcode.com/2025) aan de slag te gaan.

Hou je van programmeren en wil je zo aan het einde van het jaar eens proberen leuke puzzels op te lossen? Ga dan gerust eens aan de slag met de puzzels van Advent of Code! Iedere puzzel van Advent of Code geeft je bepaalde input-gegevens. Een dag geeft je meestal twee puzzels / parts waarbij je met die input-gegevens een oplossings moet vinden.

In dit startertemplate hebben we een paar handige functies geschreven zodat je snel aan de slag kunt. De puzzels van dag 1 zijn voorgedaan, zodat je kunt zien hoe / waar je de code om te puzzels op te lossen kunt gebruiken. Voor puzzels van dag 2 moet je zelf de input kopiëren en plakken in input.txt in de map `day02` en de code verder aanvullen. Vanaf dag 2 - part 2 moet je het zelf oppakken.


## Hoe ga je te werk?

### 1. Maak een map voor iedere dag

In de map `days` maak je voor iedere dag een nieuwe map aan, bijvoorbeeld:

```
days/day01/
```

### 2. Maak bestanden voor de puzzel

Voor ieder deel van de puzzel maak je een los Python-bestand aan (`part1.py`, `part2.py`) met de volgende startcode:

```py
import os
import hulpfuncties

# Lees input.txt uit dezelfde map als dit bestand
input = hulpfuncties.lees_bestand(os.path.dirname(__file__), "input.txt")
```

### 3. Voeg de puzzel-input toe

Maak een bestand genaamd `input.txt` in dezelfde map en plak hier de input van de puzzel in.

### 4. Code uitvoeren en debuggen

1. Open het Python-bestand dat je wilt runnen.
2. Ga naar **Uitvoeren en debuggen** in de linkerzijbalk (het icoontje met het driehoekje en het kevertje).
3. Click op het play-symbool (naast 'Run huidig bestand'; misschien is deze tekst niet helemaal zichtbaar). 
4. Gebruik in je code `print()` om variabelen of uitkomsten te printen in de debugconsole. Met behulp van formatting strings
   kun je gemakkelijk variabelen afdrukken door ze in `{ }` te zetten: `print(f"De waarde van x is: {x}")`
5. Gaat er iets niet correct en wil je stap voor stap door je code heen? Voeg dan een 'breakpoint' toe door
   naast het regelnummer van een regel code te klikken. Er verschijnt dan een rood puntje naast het regelnummer.
   Wanneer de uitvoering bij die regel is aanbeland, pauzeert de uitvoering en kun je regel voor regel de code laten uitvoeren.
   Je kunt waarden van variabelen inspecteren en als je genoeg hebt gezien de gewone uitvoering weer laten hervatten.

### Tips

* Begin altijd met het lezen van de input en omzetten naar een geschikt formaat (regels of getallen) met de hulpfuncties.
* Houd per dag één map aan zodat je overzicht behoudt.
* Run & Debug werkt automatisch op het bestand dat openstaat.
* Commit en sync als je stopt, zodat je geen werk kwijtraakt doordat een codespace verwijderd wordt.