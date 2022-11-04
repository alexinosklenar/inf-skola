import random

i=10
#><
while i<26:
    print(i, end=",")
    i=i+1

print()

j=30
while j>14:
    print(j, end=",")
    j=j-1

print()

x=""
y=""
i=0
a=0
while x !="e":
    if x=="a":
        a=a+1
    x=input("zadaj pismeno: ")
    y=y+x
    i=i+1

print ("stlacil si e....")
print(y)
print("napisal si",i, "čisel")
print("zadal si pismeno a",a, "krát")