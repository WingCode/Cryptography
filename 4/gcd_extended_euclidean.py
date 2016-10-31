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
        return x % m,g,x,y

r0=int(raw_input("Enter the 1st no "))
r1=int(raw_input("Enter the 2nd no "))

if r0>r1:
	temp=r1
	r1=r0
	r0=temp

m,g,x,y=modinv(r0,r1)
print("%dx%d + %dx%d=1"%(r0,x,r1,y))
print("Inverse is %d"%(m))