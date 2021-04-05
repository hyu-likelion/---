a, b = input().split()
new_a = ''
new_b = ''
for i in a:
	new_a = i + new_a
for i in b:
	new_b = i + new_b
a = int(new_a)
b = int(new_b)
if (a > b):
	print(a)
else:
	print(b)
