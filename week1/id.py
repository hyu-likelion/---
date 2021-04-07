def solution(new_id):
    cantchar = "~!@#$%^&*()=+[{]}:?,<>/"
    for x in cantchar:
        new_id = new_id.replace(x,"").lower()
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    if new_id[0] == ".":
        new_id = new_id[1:]
    if new_id != "" and new_id[-1] == ".":
        new_id = new_id[:-1]
    if new_id == "":
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[0] == ".":
        new_id = new_id[1:]
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id+=new_id[-1]
    return new_id