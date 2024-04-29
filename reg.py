import random
import operator
import sys


def pozdrav():
    print("Pozdravljen!\n")
    while True:
        name = (input("Vnesi svoje ime:\n"))

        if name == '':
            print("KAKŠNO JE TVOJE IME??!?!?!?!?!??!?!?")
        else:
            print("Pozdravljen/a", name)
            break


pozdrav()


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


def odgovor1(odgovor):
    while True:
        if odgovor == True:
            print("Pravilno!")
            print("Bi ponovno poskusil?\n")
            break
        else:
            print("Napaèno")
            print("Bi ponovno poskusil?\n")
            break


def askQuestion():
    odgovor = randomCalc()
    guess = float(input("Ugani? "))
    odgovor1(guess == odgovor)


def dovoljenje():
    print("Si pripravljen za matematiko?\n")

    while True:
        gameChoice = input("Da/Ne\n")

        if gameChoice == "Da":
            print("To je fantasticno")
            askQuestion()

        elif gameChoice == "Ne":
            print("Nasvidenje")
            break
        else:
            print("Da ali Ne!?!??!?!?!??!?!?")
            continue


dovoljenje()


def odgovor2():
    while True:
        gameCHOICE = input("Da/Ne\n")

        if gameCHOICE == "Da":
            randomCalc()
        else:
            sys.exit()


odgovor2()