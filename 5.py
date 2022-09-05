# Be användaren ange vilken kategori den tillhör-vuxen, pensionär, student. Om den är

# pensionär eller student kostar resan 20 kr . Om den är vuxen kostar resan 30 kr . Annars

# skall användaren informeras att den har angett en felaktig kategori.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["year"])
# IF #5

# Be användaren ange vilken kategori den tillhör-vuxen, pensionär, student. Om den är

# pensionär eller student kostar resan 20 kr . Om den är vuxen kostar resan 30 kr . Annars

# skall användaren informeras att den har angett en felaktig kategori.
kategori = input("Vilken kategori tillhör du?")
if kategori == "vuxen":
    print("Din resa kommer kosta 30 kronor")
elif kategori == "pensionär":
    print("din resa kommer att kosta 20 kronor")
elif kategori == "student":
    print("din resa kostar 20 kronor")
else:
    print("Du får fan inte köpa en biljett, stick härifrån")
