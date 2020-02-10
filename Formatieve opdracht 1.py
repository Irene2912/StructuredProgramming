#opdracht 1
def piramide():
    lengte = input("Hoe groot?")
    piramid = "";
    for amount in range(int(lengte)):
        piramid += "*"
        print(piramid)

    for amount in range(int(lengte)):
        piramid = piramid[:-1]
        print(piramid)
#joey hielp me
piramide()

#opdracht 1
def verschil():
    string1 = input("Geef een zin: ")
    string2 = input("Geef een zin: ")

    index = 0

    for c in string1:
        if len(string2) > 0:
            if c == string2[index]:
                index = index + 1
            else:
                print("het verschil zit op index: " + str(index))
                break
#joey hielp me
verschil()

#opdracht 3
def count():
    list1 = []
    list2 = [6, 8, 9, 1, 13, 6, 25]
    list3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # oprdacht a
    number1 = input("Geef een cijfer: ")
    number2 = input("Geef een cijfer: ")
    number3 = input("Geef een cijfer: ")
    number4 = input("Geef een cijfer: ")
    number5 = input("Geef een cijfer: ")
    number6 = input("Geef een cijfer: ")
    list1.append(number1)
    list1.append(number2)
    list1.append(number3)
    list1.append(number4)
    list1.append(number5)
    list1.append(number6)
    tel = list1.count(input("Welk nummer uit de lijst wil je tellen? "))
    print(tel)

    # oprdacht b
    list2.sort()
    difference = max(list2) - min(list2)
    print("het verschil tussen " + str(min(list2)) + " en " + str(max(list2)) + " is " + str(difference) + ".")

    # opdracht c
    een = list3.count(1)
    nul = list3.count(0)
    if een > nul and nul < 12:
        print("De lijst is goed.")
    else:
        print("De lijst is niet goed.")


count()

#opdracht 4
def reverse():
    woord = input("Geef een woord: ")
    different = woord[::-1]
#wist niet meer hoe je een woord moest reversen
#heb https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python gebruikt voor de slice
    print(different)

    if woord == different:
        print(woord, "is een palindroom.")
    else:
        print(woord, "is geen palindroom.")

reverse()

#opdracht 5
def sorteer():
    list = []
    number1 = input("Geef een cijfer: ")
    number2 = input("Geef een cijfer: ")
    number3 = input("Geef een cijfer: ")
    number4 = input("Geef een cijfer: ")
    number5 = input("Geef een cijfer: ")
    list.append(number1)
    list.append(number2)
    list.append(number3)
    list.append(number4)
    list.append(number5)
    list.sort()
    print(list)

sorteer()

#opdracht 6
def gemiddelde():
    list = []
    number1 = input("Geef een cijfer: ")
    number2 = input("Geef een cijfer: ")
    number3 = input("Geef een cijfer: ")
    number4 = input("Geef een cijfer: ")
    number5 = input("Geef een cijfer: ")
    list.append(int(number1))
    list.append(int(number2))
    list.append(int(number3))
    list.append(int(number4))
    list.append(int(number5))
    totaal = sum(list)
    gemid = totaal/5
    print("Het gemiddelde is: ", str(gemid))

gemiddelde()

#opdracht 7
def willekeurig():
    import random
    while 0==0:
        nummer = random.randrange(1, 11)
        gok = input("Geef een nummer tussen 1 en 10: ")
        if int(gok) != nummer:
            print(nummer)
            print("Je hebt niet juist gegokt.")
        elif int(gok) == nummer:
            print(nummer)
            print("Je hebt juist gegokt.")
            break
willekeurig()

#opdracht 8
def compression():
    file = open("compression", "rt")
    content = file.readlines()
    for i in content:
        if "\n" in content:
            content.remove("\n")
    for i in content:
        nieuw = i.strip(" \n")
        print(nieuw)

#guy hielp me
compression()

ch = input("Geef de bitjes: ")
n = input("Geef de verschuiving: ")

#opdracht 9
def verschuiven(ch, n):
    if int(n) > 0:
        for i in range(int(n)):
            char = ""
            for x in ch[-6:]:
                char += x
            char += ch[0]
            ch = char
        print(ch)
    else:
        for i in range(int(n)*-1):
            char = ""
            char += ch[-1]
            for x in ch[:6]:
                char += x
            ch = char
        print(ch)

#ruben hielp me heel erg
verschuiven(ch, n)

#opdracht 10
def fibonacci():
    a = 1
    b = 1
    lengte = input("geef de lengte: ")
    for i in range(int(lengte)):
        c = a

        a = b + a
        b = c
        print (a)
#joey hielp me
fibonacci()

#opdracht 11
def caesar():
    text = input("Geef een tekst: ")
    rotatie = int(input("Geef de rotatie: "))
    result = ""
    for i in range(len(text)):
        letter = text[i]
        if letter.isupper():
            result += chr((ord(
                letter) + rotatie - 65) % 26 + 65)
            # Formule uit: https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
        elif letter.isspace():
            result += " "
        else:
            result += chr((ord(letter) + rotatie - 97) % 26 + 97)
    print(result)
#van ruben :)
caesar()

#opdracht 12
def fizzbuzz():
    for i in range (0, 100):
        if int(i) % 3 == 0 and int(i) % 5 == 0:
            print("FizzBuzz")
        elif int(i) % 3 == 0:
            print("Fizz")
        elif int(i) % 5 == 0:
            print("Buzz")
        else:
            print(i)
#hulp van ruben
fizzbuzz()