def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append('')
    for x in range(0,len(participant)):
        if participant[x] != completion[x]:
            return(participant[x])
            break
