prijzen = {
    "aardbij": 3,
    "vanille": 4,
    "chocolade": 5
}
aanbiding = prijzen["aardbij"] * 0.8
reclame_tekst = f"Vandaag in de aanbiding: vanille-ijs, 1 liter - slechts € {aanbiding}"
reclame_tekst2 = reclame_tekst[:36]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split()
for el in reclame_tekst4:
    print(el.lower())
    if len(el) >= 5:
        print(el.upper())