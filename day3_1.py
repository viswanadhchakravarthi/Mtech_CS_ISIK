n = eval(input("Enter value of n: "))
lower = list(map(int,input("Enter lower bound: ").split(".")))
for i in lower:
	if i>9:
		print("invalid lower limit")
		exit()
upper = list(map(int,input("Enter upper bound: ").split(".")))
for i in upper:
	if i>9:
		print("invalid upper limit")
		exit()
if len(lower) < n:
	tmp = n-len(lower)
	while tmp:
		lower.append(0)
		tmp-=1
elif len(lower) > n:
	tmp = len(lower) - n
	while tmp:
		lower.pop()
		tmp -= 1
		
if len(upper) < n:
	tmp = n-len(upper)
	while tmp:
		upper.append(0)
		tmp-=1
elif len(upper) > n:
	tmp = len(upper) - n
	while tmp:
		upper.pop()
		tmp -= 1

tmp = 0
for l in lower:
	tmp = tmp*10 + l
lower = tmp

tmp = 0
for m in upper:
	tmp = tmp*10 + m
upper = tmp

# print("lower: ",lower)
# print("upper: ",upper)

for ver in range(lower,upper+1):
	ver = '.'.join([char for char in str(ver)])
	print(ver)

