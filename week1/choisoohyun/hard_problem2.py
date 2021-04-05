c = int(input())
for i in range(c):
	li = list(map(int, input().split()))
	sum = 0
	for j in range(li[0]):
		sum = sum + li[j + 1]
	mean = sum / li[0]
	count = 0
	for j in range(li[0]):
		if (li[j + 1] > mean):
			count = count + 1
	result = (count / li[0]) * 100
	print("%0.3f%%" % result)
