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
    
    def combinatie(invoer_lijst_2):
        korte_lijst = laag_en_hoog(invoet_lijst_2)
        uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
        return uitvoer