def solution(participant, completion):
    a = []
    for i in range(len(participant)):
        for j in range(len(completion)):
            if participant[i] != completion[j]:
                a.append(participant[i])
                return a
            else:
                continue


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))