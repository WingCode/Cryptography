#Inverse of a matrix
import numpy as np

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

m=int(raw_input("Enter the dimension"))
input_A=[[0 for j in range(m)] for i in range(m)]
#print input_A

for i in range(0,m):
	for j in range(0,m):
		input_A[i][j]=int(raw_input());
A=np.array(input_A)
deter=np.linalg.det(A)
adj_A=(np.linalg.inv(A)*deter)
#print adj_A
if deter<0:
	deter=deter*-1
	adj_A=adj_A*-1
#print (modinv(deter,26))	
final_A=(adj_A*modinv(deter,26))%26

print final_A