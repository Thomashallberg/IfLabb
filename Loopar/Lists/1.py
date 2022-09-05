
Tallista = []
for i in range(4):
    tal = int(input("skriv in ett tal"))
    Tallista.append(tal)
    largestSoFar = 0
    for i in Tallista:
        if i > largestSoFar:
            largestSoFar = i
print(largestSoFar)
    