from __future__ import division
import random
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

def prime_checker(t):
	if t%2==0 and t!=2 or t==1: 
		return False,t

	upper_bound=int(math.floor(math.sqrt(t)))
	for i in range(upper_bound,1,-1):
		if t%i==0:
			return False,t	
	return 	True,t


# print(prime_checker(137))

range_primes=1000
while True:
	result1=False
	result2=False
	result3=False	
	while result1==False:
		p=random.randrange(range_primes)
		result1,p=prime_checker(p)

	while result2==False:
		q=random.randrange(range_primes)
		result2,q=prime_checker(q)

	if p==q:
		continue
	
	if p>q:
		temp=q
		q=p
		p=temp

	print("The p and q are: ",p,q)
	n=p*q
	print("The n is: ",n)
	phi_n=(p-1)*(q-1)
	print("The phi_n is: ",phi_n)

	while result3==False:
		e=random.randrange(phi_n)
		result3,e=prime_checker(e)
		if e==p or e==q:
			result3=False

	print("The e is: ",e)
	m,g,x,y=modinv(e,phi_n)
	d=m
	print("The d is: ",d)

	PT="abcdefg"
	print("The original string is ",PT)
	CT=[]
	for i in range(0,len(PT)):
		CT.append(pow(ord(PT[i]),d)%n)

	print("Encrypted",CT)
	decrypt=[]
	for i in range(0,len(CT)):
		decrypt.append(chr(pow(CT[i],e)%n))

	print("The decryptes string",decrypt)
	break

	
