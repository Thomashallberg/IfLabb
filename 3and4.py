# IF #3

# Be användaren mata in två tal.number1 och number2.

# Lagra det STÖRSTA talet av dom två i en tredje variabel, largest

 

# Skriv ut: 

# Det största talet är <>
tal1 = float(input("tal1"))
tal2 = float(input("tal2"))
tal3 = float(input("tal3"))
if (tal1>tal2)and(tal1>tal3):
    print("largest=", tal1)
elif (tal2)>(tal3) and (tal2)>(tal1):
    print("largest=", tal2)
else:
    print("largest=", tal3)