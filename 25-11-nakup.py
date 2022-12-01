a=[0]*5
b=[0]*5
for i in range(5):
    a[i]=input("zadaj produkt: ")
    b[i]=int(input("zadaj cenu: "))
print(a)
print(b)

for i in range(5):
    if b[i]==3:
        print("3€ stoji:",a[i])

for i in range(5):
    b[i]=b[i]*1.2

print(a)
print(b)


for i in range(5):
    if a[i]=="alpro":
        a[i]="rajo"
        b[i]=1

print(a)
print(b)
maslo=0
sunka=0
for i in range(5):
    if a[i]=="maslo":
        maslo=i
        cenamaslo=b[i]
for i in range(5):
    if a[i]=="sunka":
        sunka=i
        cenasunka=b[i]

a[maslo]="sunka"
a[sunka]="maslo"
b[sunka]=cenamaslo
b[maslo]=cenasunka

print(a)
print(b)


