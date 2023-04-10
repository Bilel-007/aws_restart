# exercice 2
i = 0
E = int(input('Saisie ton entier positif :'))
if E < 0 :
    print("Ton saisie n'est pas un entier positif")
else :
        B = E
        while B % 2 == 0 :
                B = B/2
                i = i + 1
                print (i)
        print("{} est {} fois divisble par 2".format(E,i))