def is_reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s=input("Enter the string ")
print("Mirror image: ", end="")
print(is_reverse(s))
