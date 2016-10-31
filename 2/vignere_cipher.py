#Vignere cipher
from __future__ import print_function
import random

PT_string=(raw_input("Enter the plaintext string "))
PT=list(PT_string)
K=(raw_input("Enter the key "))

key=open('./key_vignere','w+')
print(K,file=key)
key.close()

k=0
CT=[]
for i in range(0,len(PT)):
	if k==len(K):
		k=0
	print (k,i)
	CT.append(chr((((ord(PT[i])-97)+ord(K[k])-97)%26)+65))
	k=k+1

print(CT)

