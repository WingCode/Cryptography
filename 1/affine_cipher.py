n=26
PT=raw_input("Enter the plain text string")
k=int(raw_input("Enter the key"))
PT_char=list(PT)

 
for i in range(0,len(PT_char)):
	PT_char[i]=chr((((ord(PT_char[i])+k)%n)*k)%n+97)

print (PT_char)