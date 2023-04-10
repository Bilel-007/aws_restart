# exercice 3
import random
def listAleaInt(n,a,b):
        arr = []
        while len(arr)<=n :
                arr.append(random.randint(a,b))
        print("votre liste est comme suit: ", arr)
        index=arr.index(min(arr))
        print("le minimum de cette liste à pour index :", index)
        L=arr[0]
        arr[0]=arr[index]
        arr[index]=L
        print("le tableau sera comme suit :", arr)
        return arr
n = int(input("donner le nbr des élements :"))
a = int(input("donner par où commencer "))
b = int(input("donner par où finir "))
listAleaInt(n,a,b)