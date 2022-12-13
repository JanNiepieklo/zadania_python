"""Aplikacja która przelicza wartość kilku kryprowalut na PLN. Program powinien
zawierać pola wejściowe
-kurs USD, kurs BTC/USD,
-kurs kryptowaluta/BTC i ilość poszczególnych kryptowalut
oraz
-pole tekstowe, w którym pojawi się sumaryczna wartość kryprowalut w PLN.
Zabezpieczyć program przed wprowadzeniem błędnych
danych, wykorzystując okna dialogowe."""

from tkinter import *
from tkinter import messagebox

class ZaMalaError(Exception):
    pass

class Przelicznik(object):
    def __init__(self):
        self.okno = Tk()
        self.okno.geometry("500x400")
        self.okno.title("Przelicznik kryptowalut")
        self.utworz_widgety()
        self.okno.mainloop()

    def utworz_widgety(self):
        'Utworzenie pustych Frame\'ów dla odpowiedniego ułożenia elementów w oknie'
        for i in range(10):
            if i==4:
                Frame(self.okno, width=5, height=25).grid(row=0, column=i)
            else:
                Frame(self.okno, width=20, height=25).grid(row=0, column=i)
        for j in range(15):
            Frame(self.okno, width=20, height=25).grid(column=0, row=j)

        'Utworzenie pól dla kursów USD/PLN i BTC/USD'
        self.etykietaPLN = Label(self.okno)
        self.etykietaPLN["text"] = "Kurs USD/PLN:"
        self.etykietaPLN.grid(row=2, column=2, sticky=E)
        self.polePLN = Entry(self.okno, width=12)
        self.polePLN.grid(row=2,column=3, sticky=W)

        self.etykietaBTC = Label(self.okno)
        self.etykietaBTC["text"] = "Kurs BTC/USD:"
        self.etykietaBTC.grid(row=3, column=2,sticky=E)
        self.poleBTC = Entry(self.okno, width=12)
        self.poleBTC.grid(row=3, column=3, sticky=W)


        'Utworzenie pól dla kursów kryptowalut'
        self.etykieta11 = Label(self.okno)
        self.etykieta11["text"] = "Kurs Waluta1/BTC:"
        self.etykieta11.grid(row=5, column=2, sticky=E)
        self.pole11 = Entry(self.okno, width=12)
        self.pole11.grid(row=5, column=3, sticky=W)

        self.etykieta21 = Label(self.okno)
        self.etykieta21["text"] = "Kurs Waluta2/BTC:"
        self.etykieta21.grid(row=6, column=2, sticky=E)
        self.pole21 = Entry(self.okno, width=12)
        self.pole21.grid(row=6, column=3, sticky=W)

        self.etykieta31 = Label(self.okno)
        self.etykieta31["text"] = "Kurs Waluta3/BTC:"
        self.etykieta31.grid(row=7, column=2, sticky=E)
        self.pole31 = Entry(self.okno, width=12)
        self.pole31.grid(row=7, column=3, sticky=W)

        self.etykieta41 = Label(self.okno)
        self.etykieta41["text"] = "Kurs Waluta4/BTC:"
        self.etykieta41.grid(row=8, column=2, sticky=E)
        self.pole41 = Entry(self.okno, width=12)
        self.pole41.grid(row=8, column=3, sticky=W)

        self.etykieta51 = Label(self.okno)
        self.etykieta51["text"] = "Kurs Waluta5/BTC:"
        self.etykieta51.grid(row=9, column=2, sticky=E)
        self.pole51 = Entry(self.okno, width=12)
        self.pole51.grid(row=9, column=3, sticky=W)


        'Utworzenie pól ddla ilości kryptowalut'
        self.etykieta12 = Label(self.okno)
        self.etykieta12["text"] = "Ilość Waluty1:"
        self.etykieta12.grid(row=5, column=5, sticky=E)
        self.pole12 = Entry(self.okno, width=12)
        self.pole12.grid(row=5, column=6, sticky=W)

        self.etykieta22 = Label(self.okno)
        self.etykieta22["text"] = "Ilość Waluty2:"
        self.etykieta22.grid(row=6, column=5, sticky=E)
        self.pole22 = Entry(self.okno, width=12)
        self.pole22.grid(row=6, column=6, sticky=W)

        self.etykieta32 = Label(self.okno)
        self.etykieta32["text"] = "Ilość Waluty3:"
        self.etykieta32.grid(row=7, column=5, sticky=E)
        self.pole32 = Entry(self.okno, width=12)
        self.pole32.grid(row=7, column=6, sticky=W)

        self.etykieta42 = Label(self.okno)
        self.etykieta42["text"] = "Ilość Waluty4:"
        self.etykieta42.grid(row=8, column=5, sticky=E)
        self.pole42 = Entry(self.okno, width=12)
        self.pole42.grid(row=8, column=6, sticky=W)

        self.etykieta52 = Label(self.okno)
        self.etykieta52["text"] = "Ilość Waluty5:"
        self.etykieta52.grid(row=9, column=5, sticky=E)
        self.pole52 = Entry(self.okno, width=12)
        self.pole52.grid(row=9, column=6, sticky=W)

        
        self.przycisk = Button(self.okno, width=10, height=1)
        self.przycisk["text"] = "PRZELICZ"
        self.przycisk["command"] = self.przelicz
        self.przycisk.grid(row=12, column=3)

        self.etykietaWynik = Label(self.okno)
        self.etykietaWynik["text"] = "Wartość kryptowalut w PLN:"
        self.etykietaWynik.grid(row=11, column=5)
        self.poleWynik = Entry(self.okno, width=15)
        self.poleWynik.grid(row=12, column=5, sticky=N)


    def przelicz(self):
        self.poleWynik.delete(0, END)

        'Zebranie wartości z pól kursów kryptowalut i sprawdzenie ich poprawności'
        kursy = [0,0,0,0,0]
        for i in range(0,5):
            try:
                if eval("self.pole"+str(i+1)+"1").get() != "":
                    kursy[i]=eval("self.pole"+str(i+1)+"1").get()
                if float(kursy[i]) < 0:
                    kursy[i] = 0
                    raise ZaMalaError
            except ValueError:
                messagebox.showinfo("Błąd", "Podany kurs waluty musi być liczbą")
            except ZaMalaError:
                messagebox.showinfo("Błąd", "Kurs dla waluty nie może być mniejszy od 0")


        'Zebranie wartości z pól ilości kryptowalut i sprawdzenie ich poprawności'
        ilosci = [0,0,0,0,0]
        for i in range(0,5):
            try:
                if eval("self.pole"+str(i+1)+"2").get() != "":
                    ilosci[i]=eval("self.pole"+str(i+1)+"2").get()
                if float(ilosci[i]) < 0:
                    ilosci[i] = 0
                    raise ZaMalaError
            except ValueError:
                messagebox.showinfo("Błąd", "Podana ilość waluty musi być liczbą")
            except ZaMalaError:
                messagebox.showinfo("Błąd", "Ilość waluty nie może być mniejsza od 0")


        'Zebranie wartości z pól BTC/USD i USD/PLN i sprawdzenie ich poprawności'
        BTC = 0
        USD = 0
        wynik = 0
        for i in range(5):
            BTC += float(kursy[i]) * float(ilosci[i])
        try:
            if self.poleBTC.get() != "":
                USD = BTC * float(self.poleBTC.get())
            if float(self.poleBTC.get()) < 0:
                USD = 0
                raise ZaMalaError
        except ValueError:
                messagebox.showinfo("Błąd", "Kurs BTC/USD musi być liczbą")
        except ZaMalaError:
                messagebox.showinfo("Błąd", "Kurs BTC/USD nie może być mniejszy od 0")

        try:
            if self.polePLN.get() != "":
                wynik = USD * float(self.polePLN.get())
            if float(self.polePLN.get()) < 0:
                wynik = 0
                raise ZaMalaError                   
        except ValueError:
                messagebox.showinfo("Błąd", "Kurs USD/PLN musi być liczbą")
        except ZaMalaError:
                messagebox.showinfo("Błąd", "Kurs USD/PLN nie może być mniejszy od 0")

        self.poleWynik.insert(0, "{:.2f}".format(wynik))
        
k = Przelicznik()
