import random
choice = input("continue? yes/y/n")
while choice == "yes" or choice == "y":
    print(random.randint(1, 6))
    choice = input("continue? yes/y/n")