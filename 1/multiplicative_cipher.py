#Shift cipher
n=26
PT=raw_input("Enter the plain text string ")
k=int(raw_input("Enter the key "))
PT_char=list(PT)
 
for i in range(0,len(PT_char)):
	print((ord(PT_char[i])*k)%26+97)
	PT_char[i]=chr((ord(PT_char[i])*k)%26+97)

print (PT_char)
