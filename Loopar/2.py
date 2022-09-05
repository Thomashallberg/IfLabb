# Skapa ett program där användaren får mata in två tal. Låt sedan programmet skriva ut alla

# tal som finns mellan dessa två tal på skärmen. Lös detta med en for-loop. Lös den igen med en While-loop
tal1 = int(input("skriv ett tal mellan 1 och 100"))
tal2 = int(input("skriv ett tal till mellan 1 och 100"))

#for x in range(tal1, tal2)[1:]: #slicing är fucking oläsbart :>
 #   print(x)

x=tal1
while (x<tal2-1):
    x=x+1
    print(x)


# for x in range(tal1+1, tal2):
#     print(x)