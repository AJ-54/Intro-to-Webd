a=int(input("Enter the first integer:"))
b=int(input("Enter the second integer:"))
arr1=[]
arr2=[]
arr=[]
for i in range(1,a):
	if a%i==0:
		arr1.append(i)

for j in range(1,b):
	if b%j==0:
		arr2.append(j)

for x in arr1:
	if x in arr2:
		arr.append(x)

gcd=max(arr)
print("The gcd is:",gcd)