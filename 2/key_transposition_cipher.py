from __future__ import print_function,division
import math

PT_string=(raw_input("Enter the plaintext string "))
PT=list(PT_string)
K=[3,1,4,5,2]
CT=[]

key=open('./key_transp','w+')
print(K,file=key)
key.close()
setter=0
len_K=len(K)
if len(PT)%len_K!=0:
	i=len_K
	while (i%len_K)==0:
		PT.append('z')
		i=i+1

print("Modified PT",PT)
for i in range(0,len(PT)):
	

	pos=K[i%len_K]+((len_K)*setter)-1
	if(i%len_K==len_K-1):
		setter=setter+1
	print(i,i%len_K,K[i%len_K],pos)
	#print(i,pos,setter)
	
	CT.append(PT[pos])
	print(PT[pos])

print(CT)
'''
#decrypt same
for i in range(0,len(CT)):
	if k==len(K)-1:
		k=0

	index1=K.index(K[k])
	PT_found.append(chr(ord(CT_given[int(math.floor(i/(len(K)-1))+index1)])+32))
	k=k+1

#decrypt
CT_given="TGEEMNELNNTDROEOAAHDOETCSHAEIRLM"
CT_given=list(CT_given)

PT_found=[]
k=0
for i in range(0,len(CT_given)):
	if k==len(K)-1:
		k=0

	index1=K.index(K[k])
	PT_found.append(chr(ord(CT_given[int(math.floor(i/(len(K)-1))+index1)])+32))
	k=k+1

print(PT_found)
'''
