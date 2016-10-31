from __future__ import division
import math

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return -1
    else:
        return x % m

NO=int(raw_input("Enter the number of equations "))

a=[]
n=[]
M=1
for i in range(0,NO):
    a.append(int(raw_input("Enter a")))
    n.append(int(raw_input("Enter n")))
    M=M*n[i]

M_n=[]
M_inv=[]
x=0
for i in range(0,NO):
    M_n.append(M/n[i])
    M_inv.append(modinv(M_n[i],n[i]))
    x=x+a[i]*M_n[i]*M_inv[i]

x=x%M
print(x)


