def student_func(x):
    if x % 3 == 0 and x % 5 == 0:
        a = "threefive"
    elif x % 3 == 0:
        a = "three"
    elif x % 5 == 0:
        a = "five"
    else:
        a = x
    return a
    pass


print(student_func(105))
