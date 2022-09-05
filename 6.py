# IF #6

# Be användaren mata in sitt födelseår. Om det är större eller lika med 1980 men

# mindre än 1990 skriv ut –Du är född på 1980-talet. Om det är mindre än 2000 men

# större än eller lika med 1990 skriv ut- Du är född på 1990-talet. Om det är mindre

# än 1980 eller större än eller lika med 2000, skriv- Du är inte född på 1990 eller

# 1980-talen.
Birthday = int(input("What year were you born?"))
if  1980 <= Birthday < 1990:
    print("Du är ifrån 80-talet")
elif 1990 <= Birthday < 2000:
    print("Du är född på 90-talet")
elif Birthday < 1980 > 2000:
    print("Du är varken född på 80 eller 90-talet")