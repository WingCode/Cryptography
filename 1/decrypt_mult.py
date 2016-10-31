CT="wfejbyofajzeydcmrbkjrkwabkxswkjzsfq"


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

PT=['a' for i in range(0,len(CT))]
for k in range(0,26):
	inv=modinv(k,26)
	if inv!=-1:
		for i in range(0,len(CT)):
				PT[i]=chr((ord(CT[i])*inv)%26+97)
	if inv!=-1:
		print(PT)
		print("\n")