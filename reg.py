import random
import operator
import sys
name = None

def inputName():
    global name
    print("Pozdravljen!\n")
    while True:
        name = (input("Vnesi svoje ime:\n"))

        if name == '':
            print("KAKŠNO JE TVOJE IME??!?!?!?!?!??!?!?")
        else:
            print("Pozdravljen/a", name)
            break

inputName()

def randomCalc():
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.truediv}
    num1 = random.randint(0, 12)
    num2 = random.randint(1, 10)
    op = random.choice(list(ops.keys()))
    odgovor = ops.get(op)(num1, num2)
    print("Koliko je ", num1, op, num2)
    return odgovor


def checkResponse(odgovor):
    while True:
        if odgovor == True:
            print("Pravilno!")
            print("Bi ponovno poskusil?\n")
            break
        else:
            print("Napačno")
            print("Bi ponovno poskusil?\n")
            break


def handleResponse():
    odgovor = randomCalc()
    guess = float(input("Ugani? "))
    checkResponse(guess == odgovor)


def gameLoop():
    print(name + ", si pripravljen za matematiko?\n")
    while True:
        gameChoice = input("Da/Ne\n")
        if gameChoice in ["Da", "da", "d", "DA"]:
            print("To je fantasticno")
            handleResponse()
        elif gameChoice in ["Ne", "ne", "n", "NE"]:
            print("Nasvidenje " + name)
            sys.exit()
        else:
            print("Da ali Ne!?!??!?!?!??!?!?")
            continue

gameLoop()