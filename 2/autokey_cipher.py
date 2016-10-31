PT_string=raw_input("Enter the plain text string ")
PT=list(PT_string)
K=12
CT=[]

print(ord('a'))
temp=K
for i in range(0,len(PT)):
	print(chr(temp+97),ord(PT[i]))
	CT.append(chr(((ord(PT[i])-97+temp)%26)+65))
	temp=ord(PT[i])-97

print(CT)