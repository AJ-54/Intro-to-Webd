s=list(input("Enter the names with commas:").split(","))
for i in s:
	f=" "
	a=i.split(" ")
	for j in a:
		f+=j[0]
	print(f)
