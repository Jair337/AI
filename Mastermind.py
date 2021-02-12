import random
from itertools import product

alle_opties = list(product('123456', repeat=4))
counter = 1


def start():
    """Start het programma"""
    print('Welkom bij mastermind\n')
    mode = input("Klik '1' als jij zelf wilt raden, klik '2' als de computer moet raden: ")
    if mode == '1':
        zelf_raden()
    if mode == '2':
        start_simpel()

def start_simpel(code = None, feedback = None, prev_guess = None, algoritme = None, attempts = 1):
    """Laat je kiezen tussen de verschillende algoritmen"""
    if code == None:
        code = input('Voer hier je code in: ')
    if algoritme == None:
        algoritme = input('Welk algoritme wil je gebruiken? (Kies tussen "simpel" en "worst case"): ')
    if algoritme == 'simpel':
        guess = guess_1(prev_guess, feedback)
        x = ''
        guess = (x.join(guess))
        print('Computer gokt ' + str(guess))
        if guess == code:
            print('Het is gelukt! De code is: '+ guess)
            print('Ik heb er ' + str(attempts) + ' pogingen over gedaan.')
        else:
            input('Klik enter om verder te gaan.')
            feedback = gen_feedback(code, guess)
            #print(feedback)
            #print(code)
            #print(guess)
            #input('Klik enter om verder te gaan.')
            start_simpel(code, feedback, guess, 'simpel', attempts + 1)
    if algoritme == 'worst case':
        worst_case_2(alle_opties, code, 1)


def guess_1(guess, feedback = None):
    """Genereert de gok voor het simpele algoritme"""
    new_guess = []
    if feedback == None:
        return '1111'
    else:
        guess_alg = computer_gokt_simpel(feedback, guess, alle_opties)
        for i in guess_alg:
            new_guess += i
        return new_guess

def gen_feedback(code, guess):
    """Genereert feedback"""
    goede_plek = 0
    verkeerde_plek = 0
    items_not_counted_code = ''
    items_not_counted_guess = ''
    for i in range(0, 4):
        if guess[i] == code[i]:
            goede_plek += 1
        else:
            items_not_counted_code += str(code[i])
            items_not_counted_guess += str(guess[i])
    for j in items_not_counted_guess:
        if j in items_not_counted_code:
            verkeerde_plek += 1
    return [goede_plek, verkeerde_plek]

def zelf_raden():
    """De code om tegen de computer te spelen"""
    num = (str(random.randrange(1, 7)) + str(random.randrange(1, 7)) + str(random.randrange(1, 7)) +  str(random.randrange(1, 7)))
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
                print(str(tot_count) + " nummer(s) zijn goed")
                print(str(count) + ' nummer(s) zitten op de goede plek')
                """for i in correct:
                    print(i, end=' ')"""
                n = int(input("Vul 4 getallen in: "))
            elif (count == 0):
                print("Geen een getal klopt")
                n = int(input("Vul 4 getallen in: "))
        if n == num:
            print("Goedzo!")
            print("Je hebt er " + str(ctr) + " pogingen over gedaan.")

def computer_gokt_simpel(feedback, code, alle_opties):
    """Returnt de gok voor het simpele algoritme"""
    new_comb = []
    for comb in alle_opties:
        if comb == "X":
            continue
        #print(comb)
        ind_comb = alle_opties.index(comb)
        if feedback == gen_feedback(code, comb):
            for i in comb:
                new_comb += i
            alle_opties[ind_comb] = 'X'
            #print(new_comb)
            #print (alle_opties)
            return new_comb
        else:
            #print(comb)
            alle_opties[ind_comb] = 'X'
            #print(alle_opties)

def get_highest_partition(guesses, list_left):
    """Returnt de hoogste partition value van een gok (Voor de worst case strategie)"""
    fb_1 = []
    for i in list_left:
        i = ''.join(i)
        fb_1.append(gen_feedback(guesses, i))
    #print(fb_1)
    c_0_0 = (fb_1.count([0, 0]))
    c_0_1 = (fb_1.count([0, 1]))
    c_0_2 = (fb_1.count([0, 2]))
    c_0_3 = (fb_1.count([0, 3]))
    c_0_4 = (fb_1.count([0, 4]))
    c_1_0 = (fb_1.count([1, 0]))
    c_1_1 = (fb_1.count([1, 1]))
    c_1_2 = (fb_1.count([1, 2]))
    c_1_3 = (fb_1.count([1, 3]))
    c_2_0 = (fb_1.count([2, 0]))
    c_2_1 = (fb_1.count([2, 1]))
    c_2_2 = (fb_1.count([2, 2]))
    c_3_0 = (fb_1.count([3, 0]))
    c_4_0 = (fb_1.count([4, 0]))
    lst_tot = (c_0_0, c_0_1, c_0_2, c_0_3, c_0_4, c_1_0, c_1_1, c_1_2, c_1_3, c_2_0, c_2_1, c_2_2, c_3_0, c_4_0)
    #print(lst_tot)
    return max(lst_tot)


def worst_case_2(list_left, code, counter):
    """Runt het worst case algoritme"""
    input('enter')
    guess = make_guess(list_left)
    print(f'Ik gok {guess}')
    if guess == code:
        print(f'Het is me gelukt!\nDe code is {guess}')
    else:
        input('Klik op enter.')
        temp_list = (guess[0], guess[1], guess[2], guess[3])
        fb = gen_feedback(code, guess)
        new_list = remove_impossible(list_left, code, fb)
        new_list.remove(temp_list)
        #Fprintprint(new_list)
        worst_case_2(new_list, code, counter+1)

def make_guess(list_left):
    """Returnt een gok voor het worst case algoritme"""
    dict_1 = {}
    for i in list_left:
        i = ''.join(i)
        i = str(i)
        a = str(get_highest_partition(i, list_left))
        dict_1[i] = a
    guess = (min(dict_1.items(), key=lambda x: x[1]))
    guess = guess[0]
    return guess

def remove_impossible(list_left, code, feedback_1):
    """Returnt een lijst met alle mogelijke combinaties na de gok van het worst case algoritme"""
    result = []
    temp_lst = (code[0], code[1], code[2], code[3])
    #print(temp_lst)
    for combs in list_left:
        if combs == temp_lst:
            result.append(combs)
        elif feedback_1 == gen_feedback(code, combs):
            result.append(combs)
    #print('AAAAAAAAAAAAA'+str(result))
    #print(len(result))
    return result


start()
