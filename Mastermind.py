import random
from itertools import product


# Docstrings ontbreken
# Goed gebruik van functies
# Engels en nederlands door elkaar
# Gen feedback en computer_gokt_simpel lijken nogal op elkaar, kijk of je minder duplicate code kunt krijgen.
# Bij python is camelCasing de standaard.
# Code is goed te volgen.


def start():
    print('Welkom bij mastermind\n')
    mode = input("Klik '1' als jij zelf wilt raden, klik '2' als de computer moet raden: ")
    if mode == '1':
        zelf_raden()
    if mode == '2':
        start_simpel()


def start_simpel(code=None, feedback=None, prev_guess=None, algoritme=None):
    if code == None:
        code = input('Voer hier je code in: ')
    if algoritme == None:
        algoritme = input('Welk algoritme wil je gebruiken?: ')
    if algoritme == 'simpel':
        guess = guess_1(prev_guess, feedback)
        print('Computer gokt ' + str(guess))
    if code == prev_guess:
        print('De code is ' + guess)
    else:
        input('Klik enter om verder te gaan.')
        feedback = gen_feedback(code, guess)
        print(feedback)
        print(code)
        print(guess)
        input('Klik enter om verder te gaan.')
        start_simpel(code, feedback, guess, 'simpel')


def guess_1(guess, feedback=None):
    if feedback == None:
        return '1111'
    else:
        guess_alg = computer_gokt_simpel(feedback, guess)
        return guess_alg


def alle_opties():
    return list(product('12345', repeat=4))


def gen_feedback(code, guess):
    goede_plek = 0
    verkeerde_plek = 0
    items_not_counted_code = ''
    items_not_counted_guess = ''
    for i in range(0, 4):
        if guess[i] == code[i]:
            goede_plek += 1
        else:
            items_not_counted_code += code[i]
            items_not_counted_guess += guess[i]
    for j in items_not_counted_guess:
        if j in items_not_counted_code:
            verkeerde_plek += 1
    return [goede_plek, verkeerde_plek]


def zelf_raden():
    num = (str(random.randrange(1, 6)) + str(random.randrange(1, 6)) + str(random.randrange(1, 6)) + str(
        random.randrange(1, 6)))
    num = int(num)
    print(num)
    n = int(input("Vul 4 getallen in:"))
    if (n == num):
        print("Goed geraden!")
    else:
        ctr = 0
        while (n != num):
            tot_count = 0
            ctr += 1
            count = 0
            n = str(n)
            num = str(num)
            correct = ['X'] * 4
            lst_counted = []
            for i in n:
                if i in lst_counted:
                    continue
                else:
                    tot_count += num.count(i)
                    lst_counted.append(i)
            for i in range(0, 4):
                if (n[i] == num[i]):
                    count += 1
                    correct[i] = n[i]
                else:
                    continue
            if (count < 4) and (count != 0):
                print(str(tot_count) + " nummers zijn goed")
                print(str(count) + ' nummers zitten op de goede plek')
                """for i in correct:
                    print(i, end=' ')"""
                n = int(input("Vul 4 getallen in: "))
            elif (count == 0):
                print("Geen een getal klopt")
                n = int(input("Vul 4 getallen in: "))
        if n == num:
            print("Goedzo!")
            print("Je hebt er " + str(ctr) + " pogingen over gedaan.")


def computer_gokt_simpel(feedback, guess):
    for comb in alle_opties():
        goede_plek = 0
        verkeerde_plek = 0
        items_not_counted_code = ''
        items_not_counted_guess = ''
        for i in range(0, 4):
            if guess[i] == comb[i]:
                goede_plek += 1
            else:
                items_not_counted_code += guess[i]
                items_not_counted_guess += comb[i]
        for j in items_not_counted_guess:
            if j in items_not_counted_guess:
                verkeerde_plek += 1
        if [goede_plek, verkeerde_plek] == feedback:
            return comb


start()
