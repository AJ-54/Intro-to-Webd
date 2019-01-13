test=int(input("Enter the year:"))
if (test%4)==0:
	if (test%100)==0:
		if (test%400)==0:
			print("True")
		else:
			print("False")

	else:
		print("True")

else:
	print("False")
