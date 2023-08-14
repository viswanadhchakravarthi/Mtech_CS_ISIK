def isPrime(p):
	if n<2:
		return False
	count = 0
	for i in range(1,p+1):
		if(p%i==0):
			count += 1
	if(count==2):
		return True
	else:
		return False

def generate_n_prime_numbers(n):
	res = [1]
	if n==1:
		return res
	res.append(2)
	if n==2:
		return res
	tmp = 3
	while len(res) < n:
		if(isPrime(tmp)):
			res.append(tmp)
		tmp += 1
	return res

def gen_forward(primeList,start,end):
	if(start<0):
		return
	num = primeList[start]
	for i in range(len(primeList)):
		if(i>=start and i<=end):
			print(num,end=" ")
		else:
			print(primeList[i],end=" ")
	print()
	gen_forward(primeList,start-1,end+1)

n = eval(input("Enter an odd number: "))
if n%2 == 0:
	print("Invalid number")
	exit()
siz = n//2 + 1

primeList = generate_n_prime_numbers(siz)

primeList = primeList[-1:-siz:-1] + primeList
print(primeList)
k = siz//2
gen_forward(primeList,k,k)

