def student_func(x):
    x = x.upper()
    l = 0
    r = len(x)-1
    while l < r:
        while x[l] == ' ':
            l = l + 1
        while x[r] == ' ':
            r = r-1
        if x[l] == x[r]:
            l = l + 1
            r = r-1
        else:
            return False
    return True
    pass


print(student_func("Race car"))
