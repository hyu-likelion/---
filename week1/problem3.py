a = input().upper()

def dic(a) :
    b = set(a)
    c = list(b)
    cnt = []
    num = 0
    for x in b:
        cnt.append(a.count(x))

    for y in range(0,len(cnt)):
        if cnt[y]==max(cnt):num+=1
    
    if num >= 2 : print("?")
    else : print (c[cnt.index(max(cnt))])

dic(a)
