n = eval(input("Enter an odd number: "))
if n%2 == 0:
	print("Invalid number")
	exit()

for i in range(n):
	for j in range(n):
		if(i==j or i+j==n-1):
			print("*",end="")
		else:
			print(" ",end="")
	print()
