
for j in range (6):
    for i in range (6):
        print("a", end="")
    print()

print()

for j in range (1,7):
    for i in range (1,7):
        print(i, end="")
    print()

print()

for j in range (3):
    for i in range (5,11):
        print(i,"a", end=" ")
    print()

print()

for j in range (3):
    for i in range (1,5):
        for k in range (1,5):
            print(j+1, end="")
        print()
    print()

import time
import random

sucet=0
for a in range(5,50,3):
    sucet=sucet+a
print(sucet)

sucin=1
for a in range(10,61,4):
    sucin=sucin*a
print(sucin)

print()

for l in range (1,20):
    print(random.randint(1,100), end=", ")
time.sleep(1)
