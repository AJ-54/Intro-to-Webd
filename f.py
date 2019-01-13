print("Enter the list of numbers:")
a=list(map(int,input().split()))

d={}
for x in a:
	if x not in d:
		d[x]=1
	else:
		d[x]+=1

print(d)