print("Example 1: ")

a = 5
b = 4
for i in range(a):
    for j in range(i+1):
        print('*', end=" ")
    print()
for i in range(b):
    for x in range(i, b):
        print("*", end=" ")
    print()


print("Example 2: ")

y = 7
for i in range(y):
    for m in range(i, y):
        print(" ", end=" ")

    for m in range(i+1):
        print("*", end=" ")

    for m in range(i):
        print("*", end=" ")

    for m in range(i, y):
        print(" ", end=" ")

    print()


print('Example 3: ')

G = 8
for i in range(G):
    for k in range(i, G):
        print(" ", end=" ")
    for k in range(i+1):
        print("*", end=" ")

    print()

for i in range(G):
    for k in range(i+1):
        print(" ", end=" ")
    for k in range(i, G):
        print("*", end=" ")
    print()

print('Example 4: ')

z = 9

for i in range(z):
    for a in range(i, z):
        print("*", end=" ")
    for a in range(i+1):
        print(" ", end=" ")
    print()


print("Example 5: ")

d = 7
for i in range(d):
    for h in range(i, d):
        print(" ", end=" ")
    for h in range(i+1):
        print("*", end=" ")
    for h in range(i):
        print("*", end=" ")
    for h in range(i, d):
        print(" ", end=" ")
    print()


d = 7
c = 6
for i in range(d):
    for k in range(i+1):
        print(" ", end=" ")
    for k in range(i, d):
        print("*", end=" ")
    for k in range(i, c):
        print("*", end=" ")
    for k in range(i+1):
        print(" ", end=" ")
    print()