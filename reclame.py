from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer

def inkomsten_totaal(inkomsten, btw=0):
    totaal =sum(inkomsten)

    if btw > 0:
        btw_bedrag = totaal * btw
        return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."
    else:
        return totaal
    
def laag_en_hoog(mijn_lijst):
    uitvoer = []
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer.append(laagste)
    uitvoer.append(hoogste) 
    return uitvoer   
    
def gemiddelde(mijn_lijst):
    aantal = len(mijn_lijst)
    totaal = 0
    for element in mijn_lijst:
        totaal += element
        gemiddelde = totaal / aantal
        return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
    
def meervoudig(invoer_lijst):
    tijdelijk = laag_en_hoog(invoer_lijst)    
    uitvoer = [tijdelijk[0],tijdelijk[1]]
    return uitvoer