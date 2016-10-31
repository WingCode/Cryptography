#Additive+Multiplicative cipher

cipher_range=int(raw_input("Enter the 'n' "))
number=int(raw_input("Enter the no for inverse "))
additive_inverse=number-cipher_range

if additive_inverse < 0:
	additive_inverse=additive_inverse*-1

global mul_inv

for i in range(0,cipher_range-1):
	if ((number*i)%cipher_range)== 1:
		mul_inv=i
		
		
	


print "Additive inverse is %d" %(additive_inverse)
print "Multiplicative inverse is %d"%(mul_inv)
