import math

class Prostokat(object):
    def __init__(self, a, b):
        if a>0 and b>0:
            self.a = a
            self.b = b
        else:
            print("Bok a lub bok b jest niepoprawny!")
            exit(0)


    def pole(self):
        return self.a * self.b

    def przekatna(self):
        return (self.a**2+self.b**2)**(1/2)

class Rownoleglobok(Prostokat):
    def __init__(self, a, b, k):
        super().__init__(a,b)
        if k>=0 and k<90:
            self.k = math.radians(k)
        else:
            print("Kąt niepoprawny!")
            exit(0)

    def pole(self):
        return super().pole() * math.sin(self.k)

    def przekatna(self):
        return math.sqrt((super().przekatna())**2-2*self.a*self.b*math.cos(self.k))

def main():
    p1 = Prostokat(10,5)
    r1 = Rownoleglobok(8,6,60)
    print("Pole p1:", p1.pole(), "Przekątna p1:", p1.przekatna())
    print("Pole r1:", r1.pole(), "Przekątna r1:", r1.przekatna()) 

main()
