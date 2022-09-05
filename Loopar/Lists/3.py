Tallista = [1,3,6,9,12]
for i in range(4):
    largestSoFar = 0
    for i in Tallista:
        if i > largestSoFar:
            largestSoFar = i
print(largestSoFar)