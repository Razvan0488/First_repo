'''1.
Clasa Cerc

Atribute: raza, culoare

Constructor pt ambele atribute

Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria
diametru()
circumferinta()
'''

from math import pi

class Cerc:
    def __init__(self,raza,culoare):
        self.raza= raza
        self.culoare=culoare
    def descriere_cerc(self):
        print(f'Cercul are culoarea {self.culoare} si are raza {self.raza}')
    def aria(self):
        return pi*self.raza**2
    def diametru(self):
        return 2*self.raza
    def circumferinta(self):
        return 2*pi*self.raza


cerc1 = Cerc(5, 'galben')
cerc2 = Cerc(4, 'rosu')

cerc1.descriere_cerc()
cerc2.descriere_cerc()

print(cerc1.aria())
print(cerc2.aria())

print(cerc1.diametru())
print(cerc2.diametru())

print(cerc1.circumferinta())
print(cerc2.circumferinta())

'''2. 
Clasa Dreptunghi

Atribute: lungime, latime, culoare

Constructor pt toate atributele

Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
'''

class Dreptunghi:
    def __init__(self,lungime,latime,culoare):
        self.lungime= lungime
        self.latime=latime
        self.culoare=culoare
    def descriere(self):
        print(f'Dreptunghiul are lungimea {self.lungime} ,latimea {self.latime} si culoarea {self.culoare}')
    def arie(self):
        return self.lungime*self.latime
    def perimetru(self):
        return 2*self.lungime+2*self.latime
    def schimbare_culoare(self,culoare_noua):
        self.culoare=culoare_noua

d1=Dreptunghi(5,4,'albastru')
d2=Dreptunghi(7,6,'rosu')

d1.descriere()
d2.descriere()
print(d1.arie())
print(d2.arie())
print(d1.perimetru())
print(d2.perimetru())
d1.schimbare_culoare('verde')
d2.schimbare_culoare('galben')
print(d1.culoare)
print(d2.culoare)

'''3.
Clasa Angajat

Atribute: nume, prenume, salariu

Constructor pt toate atributele

Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
'''

class Angajat:
    def __init__(self, nume, prenume,salariu):
        self.nume=nume
        self.prenume=prenume
        self.salariu= salariu
    def descriere(self):
        print(f'Angajatul are numele {self.nume} si prenumele  {self.prenume} si are salariul {self.salariu}')
    def nume_complet(self):
        print(f'Numele complet al angajatului este {self.nume} {self.prenume}')
    def salariu_lunar(self):
        print(f"Salariul lunar este {self.salariu}")
    def salariu_anual(self):
        print(f'Salariul anula este {self.salariu*12}')
    def marire_salariu(self,procent):
        self.salariu= self.salariu+ procent/100*self.salariu
a1=Angajat('Popescu','Ionel',1000)
a2=Angajat('Ionescu','Mihai',1200)
a1.descriere()
a2.descriere()
a1.nume_complet()
a2.nume_complet()
a1.salariu_lunar()
a2.salariu_lunar()
a1.salariu_anual()
a2.salariu_anual()
a1.marire_salariu(20)
a2.marire_salariu(15)
print(a1.salariu_lunar())
print(a2.salariu_lunar())

'''
4.
Clasa Cont

Atribute: iban, titular_cont, sold

Constructor pentru toate

Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
'''

class Cont:
    def __init__(self,iban,titular_cont,sold):
        self.iban=iban
        self.titular_cont=titular_cont
        self.sold=sold
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold}')
    def debitare_cont(self,suma_debitata):
        if suma_debitata > self.balance:
            print()
        else:
            self.balance -= suma_debitata
            print(f"{suma_debitata}RON has been debited from the account")

    def creditare_cont(self, suma_depusa):
            self.balance += suma_depusa
            print(f"{suma_depusa}RON has been credited to the account")

