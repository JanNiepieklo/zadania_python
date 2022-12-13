from math import *

class NiedodatniaError(Exception):
    pass

e=open("pierwiastki.txt","w")

try:
    n=int(input("Podaj liczbę naturalną n:"))
    if n<1:
        raise NiedodatniaError
except ValueError:
    print("Liczba n musi być całkowita!")
except NiedodatniaError:
    print("Liczba n musi być dodatnia!")
else:
    j=0
    for i in range(1,n+1):        
        e.write("{:.2f}".format(sqrt(i))+"\t")
        j+=1
        if j%10==0:
            e.write("\n")
e.close()
