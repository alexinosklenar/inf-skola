import time
import random

print("vitajte v keno 5")
time.sleep(1)
print("connecting to https://www.keno5.com/loteria-dnes")
time.sleep(3)
print("pripojené")
time.sleep(1)


a=int(input("zadaj 1. cislo: "))
b=int(input("zadaj 2. cislo: "))
c=int(input("zadaj 3. cislo: "))
d=int(input("zadaj 4. cislo: "))
e=int(input("zadaj 5. cislo: "))

x=0
for l in range (1,81):
    w=random.randint(1,100)
    if a==w:
        x=x+1
        a=500
    if b==w:
        x=x+1
        b=500
    if c==w:
        x=x+1
        c=500
    if d==w:
        x=x+1
        d=500
    if e==w:
        x=x+1
        e=500
    y=w
    




if x==0:
    print("nevyhral si nič ):")

if x==1:
    print("trafil si jedno číslo, vyhral si nič")

if x==2:
    print("trafil si dve čísla, vyhral si 5€")

if x==3:
    print("trafil si tri čísla, vyhral si 15€")

if x==4:
    print("trafil si štyri čísla, vyhral si 100€")

if x==5:
    print("trafil si päť čísiel, vyhral si nový Samsung Galaxy S22 Ultra")