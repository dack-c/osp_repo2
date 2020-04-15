#!/usr/bin/python3
n = int(input("fibonacci number? "))
fibs = [0 for i in range(n+1)]

fibs[1] = 1
if(n >= 2):
    fibs[2] = 1
for i in range(3, n+1):
    if (n == 1) or (n == 2):
        break
    else:
        fibs[i] = fibs[i-1] + fibs[i-2]

print(fibs[1],end='')
for i in range(2, n+1):
    print(",{}".format(fibs[i]),end='')

print("\nF{} = {}".format(n, fibs[n]))
