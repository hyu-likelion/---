def solution(participant, completion):
    a = []

    for i in participant:
        a.append(i)
    for j in completion:
        a.remove(j)

    return a[0]


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))
