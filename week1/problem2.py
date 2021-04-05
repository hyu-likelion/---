c = int(input())

def avgRat(c) :
    sum = num = 0
    score = []
    rat = []
    avg = []
    for x in range(0, c):
        score.append(list(map(int,input().split())))
        for y in range(1, len(score[x])):
            sum += score[x][y]
        avg.append(sum / score[x][0])
        for z in range(1, len(score[x])):
            if(score[x][z] > avg[x]):
                num += 1
        rat.append(num/score[x][0]*100)
        sum = num = 0

    for x in range(0, c):
        print("%.3f%%" %rat[x])

avgRat(c)
