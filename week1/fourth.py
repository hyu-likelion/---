x, y = input().split()
a = x[0]
b = x[1]
c = x[2]
d = y[0]
e = y[1]
f = y[2]
x1 = int(c + b + a)
y1 = int(f + e + d)
if x1 > y1:
    print(x1)
else:
    print(y1)
