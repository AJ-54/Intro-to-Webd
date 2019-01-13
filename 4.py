print("Enter the number:")
n=int(input())
s=str(n)
l=len(s)

def recursion_first(f1,st):
	if f1!=0 :
		return(recursion_first(f1-3,st)+","+st[(f1-2):(f1+1)])
	else:
		return st[:1]

def recursion_second(g1,st):
	if g1!=0 :
		return(recursion_second(g1-3,st)+","+st[(g1-1):(g1+2)])
	else:
		return st[:2]

def recursion_third(k1,st):
	if ((k1!=0) & (k1!=3)):
		return(recursion_third(k1-3,st)+","+st[(k1-3):(k1)])

	elif(k1==3):
		return(st[(k1-3):(k1)])

	else:
		return("")

if l<=3:
	print(l)
else:
	a=l%3
	b=l/3
	if a==1:
		f=l-1
		w=recursion_first(f,s)
	elif a==2:
		g=l-2
		w=recursion_second(g,s)
	elif a==0:
		k=l
		w=recursion_third(k,s)

print(w)

