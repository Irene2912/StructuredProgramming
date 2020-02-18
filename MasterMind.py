import random

def MasterMind():
    secretcode = []
    secretcode = random.sample(range(1, 7), 4)
    print(secretcode)

    while True:
        gok = input("Wat is de code: ")
        if  gok == secretcode:
            print("Congratz")
            break
        else:
            gok = input("Wrong code, Try again: ")


MasterMind()