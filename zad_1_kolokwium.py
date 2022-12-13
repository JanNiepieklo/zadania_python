from random import randint

def modyfikacja(a):
    for i in range(len(a)-1, -1, -1):
        if a[i]%4==0:
            del a[i]
        elif a[i]%2!=0:
            a[i]+=2
    return a

def main():
    a=[]
    for i in range(20):
        a.append(randint(100,120))

    print("Lista przed modyfikacją:\n",a)
    iloczyn=1
    for i in a:
        if i%2!=0:
            iloczyn*=i
    print("Iloczyn nieparzystych elementów listy wynosi: ", iloczyn)
    modyfikacja(a)
    print("Lista po modyfikacji:\n",a)

main()

