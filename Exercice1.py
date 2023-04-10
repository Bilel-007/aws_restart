# exercice 1
import math
pi = math.radians(180)
isdigit = False
while (not isdigit) :
        try :
                R = float(input("Saisie le rayon : "))
                H = float(input("Saisie la hauteur : "))
                V = pi*R*R*H/3
                if V :
                        isdigit = True
                print(V)
        except ValueError:
                print("Merci de donner un chiifre")