CT="beeakfydjxuqyhyjiqryhtyjiqfbqduyjiikfuhcqd"

PT=['a' for i in range(0,len(CT))]
for k in range(0,26):
	for i in range(0,len(CT)):
		PT[i]=chr((ord(CT[i])-k)%26+97)
	print(PT)
	print("\n")
