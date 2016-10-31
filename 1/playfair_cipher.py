#Playfair cipher
PT_string=raw_input("Enter the plain text string ")
K=[['L','G','D','B','A'],['Q','M','H','E','C'],['U','R','N','I','F'],['X','V','S','O','K'],['Z','Y','W','T','P']]
C=[]
#print(K)
PT=list(PT_string)
temp=PT[0];

if(len(PT)%2==1):
	PT=PT+list('x')

for i in range(1,len(PT)):
	if PT[i]==temp and i%2==1:
		PT[i]='x'

	else:
		temp=PT[i]
		
print(PT)
for no in range(0,len(PT)-1,2 ):
	for i in range(0,5):
		for j in range(0,5):
			if(ord(K[i][j])+32==ord(PT[no])):
				i_th=i
				j_th=j
				if(j_th+1==5):
					j_th=-1

				if(i_th+1==5):
					i_th=-1
				#print(i_th,j_th,no)	
				if(ord(K[i_th][j_th+1])+32==ord(PT[no+1])):
					C.append(K[i_th][j_th+1])
					if(j_th+2==5):
						j_th=-2
					C.append(K[i_th][j_th+2])

				elif(ord(K[i_th+1][j_th])+32==ord(PT[no+1])):
					C.append(K[i_th+1][j_th])
					if(i_th+2==5):
						i_th=-2
					C.append(K[i_th+2][j_th])

				else:
					first_i=i
					first_j=j
					for i in range(0,5):
						for j in range(0,5):
							if(ord(K[i][j])+32==ord(PT[no+1])):
								C.append(K[first_i][j])
								C.append(K[i][first_j])


			#print(C)		
print(C)	