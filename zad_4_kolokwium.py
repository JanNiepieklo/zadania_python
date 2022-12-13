from zope.interface import Interface, implementer
from zope.component import provideUtility, getUtility

class IBryla(Interface):
    def pole():
    def objetosc():
    def maxodleglosc():
        
@implementer(IBryla)
class Prostopadloscian(object):
    def __init__(self,a,b,h):
        if a>0 and b>0 and h>0:
            self.a=a
            self.b=b
            self.h=h
        else:
            print("Boki są niepoprawne, wprowadź dodatnie liczby!")
            exit(0)
        
    def pole(self):
        return 2*self.a*self.b+2*self.a*self.h+2*self.b*self.h
    def objetosc(self):
        return self.a*self.b*self.h
    def maxodleglosc(self):
        return (self.a**2+self.b**2+self.h**2)**(1/2)
    
@implementer(IBryla)
class Kula(object):
    def __init__(self,r):
        if r>0:
            self.r=r
        else:
            print("Promień niepoprawny, wprowadź dodatnią liczbę!")
            exit(0)
    def pole(self):
        return 3,14*(self.r**2)
    def objetosc(self):
        return 4/3*3.14*(self.r**3)
    def maxodleglosc(self):
        return 2*self.r

def main():
    provideUtility(Prostopadloscian(20,30,10), IBryla,"Bryla1")
    provideUtility(Kula(15), IBryla,"Bryla2")

    x=getUtility(IBryla,"Bryla1")
    y=getUtility(IBryla,"Bryla2")
    print("Pole prostopadłościanu: ", x.pole())
    print("Objętość prostopadłościanu: ", x.objetosc())
    print("Maksymalna odległość pomiędzy punktami w prostopadłościanie: ", x.maxodleglosc())
    print("Pole kuli: ", y.pole())
    print("Objętość kuli: ", y.objetosc())
    print("Maksymalna odległość pomiędzy punktami w kuli: ", y.maxodleglosc())
main()




    
