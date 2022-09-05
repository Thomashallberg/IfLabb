summa = int(input("hur mycket pengar har du?"))
rabatt = (input("rabatt?"))#ja/nej
if rabatt == "ja":
    rabatt = True
else: rabatt = False
if summa >= 15 and summa <= 25 and rabatt:
    print("du kan köpa en liten burgare")
elif summa  >= 15 and summa <= 25 and not rabatt:
    print("du kan köpa en liten burgare och en pommes frites..")
elif summa  >= 25 and summa <= 50 and not rabatt :
    print("du kan köpa en stor hamburgare")
elif summa >= 25 and summa <= 50 and rabatt:
    print("du kan köpa en stor burgare och pommes")
elif summa <= 60 and summa >= 50 and rabatt:
    print("du kan köpa ett meal med dryck")
elif 70 <= summa <= 80 and not rabatt:
    print("Du får köpa munk")
elif 80 < summa < 90 and not rabatt:
    print("Du får köpa milkshake")
elif 90 <= summa < 100 and rabatt == True:
    print("Du får inte köpa något :)")