def solution(new_id):
    li = ['-', '_', '.']
    new_id = new_id.lower()
    answer = ''
    for i in new_id:
        if i.isalnum() == True or i in li:
            answer += i
    while ".." in answer:
        answer = answer.replace("..",".")
    answer = answer.lstrip('.').rstrip('.')
    if answer == "":
        answer = "a"
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip('.')
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    return answer
