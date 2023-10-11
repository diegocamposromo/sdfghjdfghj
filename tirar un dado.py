import random

def dado(numero):
    if numero == 1:
        print("   |000|   ")
        print("   |0 0|   ")
        print("   |000|   ")
    elif numero == 2:
        print("   | 00|   ")
        print("   |000|   ")
        print("   |00 |   ")
    elif numero == 3:
        print("   |00 |   ")
        print("   |0 0|   ")
        print("   | 00|   ")
    elif numero == 4:
        print("   | 0 |   ")
        print("   |000|   ")
        print("   | 0 |   ")
    elif numero == 5:
        print("   | 0 |   ")
        print("   |0 0|   ")
        print("   | 0 |   ")
    elif numero == 6:
        print("   | 0 |   ")
        print("   | 0 |   ")
        print("   | 0 |   ")


azar = random.randint(1, 6)


dado(azar)