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