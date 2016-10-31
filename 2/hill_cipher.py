#Vignere cipher
from __future__ import print_function,division
import random
import math
import numpy

PT_string=(raw_input("Enter the plaintext string "))
PT=list(PT_string)
delim=int(math.ceil(len(PT_string)/4))
#print(delim)
PT_array=[['z' for i in range(0,4)] for j in range(0,delim)]
CT=[[0 for i in range(0,4)] for j in range(0,delim)]
K=[[9,7,11,13],[4,7,5,6],[2,21,14,9],[3,23,21,8]]
key=open('./key_hill','w+')
print(K,file=key)
key.close()
#print(PT_array)
k=0
for i in range(0,delim):
	for j in range(0,4):
		if k!=len(PT_string):
			#print (i,j,k)
			PT_array[i][j]=PT_string[k]
			#print (PT_array)
			k=k+1

print ("The new PT array is",PT_array)

for i in range(0,delim):
	for j in range(0,4):
		PT_array[i][j]=ord(PT_array[i][j])-97

sum1=0
for i in range(0,delim):
	for j in range(0,4):
		for k in range(0,4):
			#print(PT_array[i][k],K[k][j],"array")
			sum1=(sum1+(PT_array[i][k]*K[k][j]))
	
		CT[i][j]=sum1
		#print(CT[i][j],"value")
		sum1=0		

print(CT)
for i in range(0,delim):
	for j in range(0,4):
		CT[i][j]=chr((CT[i][j]%26)+65)




	
print(CT)	