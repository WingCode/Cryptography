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

print(prime_checker(1792))