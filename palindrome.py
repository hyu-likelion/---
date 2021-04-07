a = input().upper().replace(" ", "")

def student_func(a):
    if len(a) % 2 == 0:
        for x in range(0, int(len(a) / 2)):
            if a[x] != a[len(a) - 1 - x]:
                return False
    else:
        for x in range(0, int((len(a) - 1) / 2)):
            if a[x] != a[len(a) - 1 - x]:
                return False

    return True

print(student_func(a))