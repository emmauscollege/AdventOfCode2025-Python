import os
import hulpfuncties

# Lees input.txt uit dezelfde map als dit bestand
input = hulpfuncties.lees_bestand(os.path.dirname(__file__), "input.txt")
input_regels = hulpfuncties.tekst_naar_regels(input)

# positie van de draaiknop van de kluis. Start op 50
draai_knop_positie = 50

# aantal keer dat de draaiknop weer op 0 heeft gestaan
aantal_keer_nul = 0

# loop om alle draaiingen te doorlopen
# iedere losse input voor een draai komt in de variabele 'code' 
for code in input_regels:
    # de logging mag je weglaten, maar kan helpen om je
    # oplossing gaandeweg te controleren:
    print(f"Code is: {code}")
    print(f"Huidige positie is: {draai_knop_positie}")

    # eerste teken bepaalt richting
    link_of_rechts = code[0]
    print(f"We draaien in de richting: {link_of_rechts}")

    # rest van de string is de afstand
    draai_afstand = int(code[1:])
    print(f"De afstand die we gaan draaien is: {draai_afstand}")

    for stap in range(0,draai_afstand):
        # Nu gaan we draaien!
        if link_of_rechts == "L":
            draai_knop_positie = draai_knop_positie - 1
        else:
            draai_knop_positie = draai_knop_positie + 1

        if draai_knop_positie == -1:
            draai_knop_positie = 99

        if draai_knop_positie == 100:
            draai_knop_positie = 0
        
        # check of positie 0 is, voor de uiteindelijke oplossing
        if draai_knop_positie == 0:
            aantal_keer_nul = aantal_keer_nul + 1

        print(f"De draaiknop is tot nog toe {aantal_keer_nul} keer bij de 0 geweest")



# print de oplossing:
print(f"De draaiknop is in totaal {aantal_keer_nul} keer bij de 0 geweest")
