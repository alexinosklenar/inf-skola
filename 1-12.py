a=[0]*3
b=[0]*3
for i in range(3):
    a[i]=input("zadaj meno: ")
    b[i]=int(input("zadaj vek: "))
print(a)
print(b)

for i in range(3):
    if a[i]=="janko":
        print("janko ma",b[i],"rokov")

print(a)
print(b)

for i in range(3):
    if a[i]=="ferko":
        b[i]=b[i]+1

print(a)
print(b)
    
for i in range(3):
    if a[i]=="matko":
        a[i]="anna"
        b[i]=15

print(a)
print(b)

pocet15=0
for i in range(3):
    if b[i]==15:
        pocet15=pocet15+1

print("pocet deti s vekom 15r: ",pocet15)

for i in range(3):
    if a[i]=="ferko":
        print("ferko",i)

vek=0
for i in range(3):
    vek=vek+b[i]

print("priemer je:",vek/3)

pocet18=0
for i in range(3):
    if b[i]>=18:
        pocet18=pocet18+1

print("pocet dospelych deti je: ",pocet18)

for i in range(3):
    if a[i]=="janko":
        jan=i
        print("janko",i)

for i in range(3):
    if i!=jan:
        print (a[i],end=",")

