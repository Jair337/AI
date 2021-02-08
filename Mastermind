import random

def zelf_raden():
    num = (str(random.randrange(1, 6)) + str(random.randrange(1, 6)) + str(random.randrange(1, 6)) + str(random.randrange(1, 6))) #Genereert random code
    num = int(num)
    print(num)
    n = int(input("Vul 4 getallen in:")) #Gebruiker vult een gok in
    if (n == num): #Als de code goed is
        print("Goed geraden!") 
    else:
        ctr = 0 #Counter die 'attempts' bijhoud
        while (n != num): #While de code niet is geraden
            tot_count = 0 #Hoeveeleid getallen die in de code zitten
            ctr += 1 #Attempts +1
            count = 0 #Hoeveelheid getallen op een goede plek
            n = str(n)
            num = str(num)
            lst_counted = [] #Houdt bij welke getallen er al zijn geteld
            for i in n: #Deze for loop checkt hoeveel getallen van de gok er ook in de code zitten
                if i in lst_counted: #Als het getal al een keer geteld is gaat de functie gewoon door
                    continue
                else:
                    tot_count += num.count(i) #Als het getal in de code zit telt deze functie hoevaak
                    lst_counted.append(i) #Dit voegt het getelde getal toe aan een lijst zodat getallen niet 2 keer worden geteld
            for i in range(0, 5):
                if (n[i] == num[i]): #Als een getal uit de gok op dezelfde index zit als de code
                    count += 1 #Gaat de 'op de goede plek counter omhoog
                else:
                    continue
            if (count != 0):
                print(str(tot_count) + " nummers zijn goed")
                print(str(count) + ' nummers zitten op de goede plek')
                n = int(input("Vul 5 getallen in: "))
            elif (count == 0):
                print("Geen een getal klopt")
                n = int(input("Vul 5 getallen ij: "))
        if n == num:
            print("Goedzo!")
            print("Je hebt er ", ctr, " pogingen over gedaan.")


zelf_raden()









