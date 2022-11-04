for i in range (0,5):
    print("piatok")

print()

for i in range (0,7):
    print(i)

print()

for i in range (0,5):
    print(i+10)


print()

sucet=0

x=int(input("zadaj cislo: "))
for x in range(x):
    print(x, end=", ")
    sucet=sucet+x

print()
print(sucet)

sucin=1
for x in range(1,10):
    sucin=sucin*x
    
print(sucin)

y=int(input("zadaj y: "))
if x<y:
    for x in range(x,y):
        print(x+1, end=", ")
