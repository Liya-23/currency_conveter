#this code for now is still one sided it only works when you convert to rands using other currencies
#country visited
print("Welcome to South Africa")
country_from = input("Whch Country Are You Visiting? United State of America(A)/EUROPE(B)/BRITAIN(C)/INDIA(D)/AUSTRALIA(E)/CANADA(F)/SINGAPORE(G)/SWISS(H)/MALASIA(I)/JAPAN(J) ")
country_origin = country_from.upper()
#get country
def getCountry():
    """
    Purpose: 
    """
    if country_origin == "A":
        return "United States Of America"
    elif country_origin == "B":
        return "Europe"   
    elif country_origin == "C":
        return "Britain"
    elif country_origin == "D":
        return "India"
    elif country_origin == "E":
        return "Australia"
    elif country_origin == "F":
        return "Canada"
    elif country_origin == "G":
        return "Singapore"
    elif country_origin == "H":
        return "Swiss"
    elif country_origin == "I":
        return "Malasia"
    elif country_origin == "J":
        return "Japan"
# end def

#exchange rates compared to ZAR
usd = 17.932954
euro = 19.957836
brit = 23.054696
inr = 0.218735
aud = 12.087837
cad = 13.560014
sid = 13.474025
swf = 20.709942
mar = 3.934277
jpy = 0.126477 

#how much you got
amount = float(input("how much money you got? "))

#call the get country method
x = getCountry()
#main conversion
def converter():
    """
    Purpose: 
    """
    if country_origin == "A":
        zar = amount * usd
        txt = "you got: R{}"
        print("You had "+ str(amount) + "usd in "+ x + " in SA " + txt.format(zar))

    elif country_origin == "B":
        zar = amount * euro
        txt = "you got: R{}"
        print("You had "+ str(amount) + "euro in "+ x + " in SA " + txt.format(zar))

    elif country_origin == "C":
        zar = amount * brit
        txt = "you got: R{}"
        print("You had "+ str(amount) + "gbp in "+ x + " in SA " + txt.format(zar))

    elif country_origin == "D":
        zar = amount * inr
        txt = "you got: R{}"
        print("You had "+ str(amount) + "inr in "+ x + " in SA " + txt.format(zar))

    elif country_origin == "E":
        zar = amount * aud
        txt = "you got: R{}"
        print("You had "+ str(amount) + "aud in "+ x + " in SA " + txt.format(zar))

    elif country_origin == "F":
        zar = amount * cad
        txt = "you got: R{}"
        print("You had "+ str(amount) + "cad in "+ x + " in SA " + txt.format(zar))

    elif country_origin == "G":
        zar = amount * sid
        txt = "you got: R{}"
        print("You had "+ str(amount) + "sid in "+ x + " in SA " + txt.format(zar))

    elif country_origin == "H":
        zar = amount * swf
        txt = "you got: R{}"
        print("You had "+ str(amount) + "swf in "+ x + " in SA " + txt.format(zar))

    elif country_origin == "I":
        zar = amount * mar
        txt = "you got: R{}"
        print("You had "+ str(amount) + "mar in "+ x + " in SA " + txt.format(zar))

    elif country_origin == "J":
        zar = amount * jpy
        txt = "you got: R{}"
        print("You had "+ str(amount) + "jpy in "+ x + " in SA " + txt.format(zar))
# end def

converter()
