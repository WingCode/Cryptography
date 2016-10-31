from __future__ import print_function,division
import math

PT_string=(raw_input("Enter the plaintext string "))
PT=list(PT_string)
K=[4,1,6,2,7,3,8,5]
CT=[]


setter=0
len_K=len(K)
if len(PT)%len_K!=0:
	i=len_K
	while (i%len_K)==0:
		PT.append('z')
		i=i+1

#print("Modified PT",PT)
for i in range(0,len(PT)):

	pos=K[i%len_K]+((len_K)*setter)-1
	if(i%len_K==len_K-1):
		setter=setter+1
	#print(i,i%len_K,K[i%len_K],pos)
	#print(i,pos,setter)
	
	CT.append(PT[pos])
	#print(PT[pos])

print(CT)

#decrypt same
PT=[]



#print(K)

setter=0
for i in range(0,len(CT)):
	if (i+1)%8==0:
		l=8

	else:
		l=(i%len_K)+1
	
	print(i,l,setter,len_K)
	pos=K.index(l)+(len_K*setter)
	if(i%len_K==len_K-1):
		setter=setter+1
	PT.append(CT[pos])

print(PT)




CT="TGEEMNELNNTDROEOAAHDOETCSHAEIRLM"
CT=list(CT)

PT=[]
setter=0
k=0
for i in range(0,len(CT)):
	if (i+1)%8==0:
		l=8

	else:
		l=(i%len_K)+1
	
	#print(i,l,setter,len_K)
	pos=K.index(l)+(len_K*setter)
	if(i%len_K==len_K-1):
		setter=setter+1
	PT.append(CT[pos])
	#print(PT)

print(PT)


