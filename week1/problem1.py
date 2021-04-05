a, b = input().split()

a = int(a[::-1])
b = int(b[::-1])

def compare(a,b):
    if a>b : print(a)
    else : print(b)

compare(a,b)
