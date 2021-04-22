def comparenumber(num1, num2):
    x = int(str(num1)[::-1])
    y = int(str(num2)[::-1])
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "same"


print(comparenumber(734, 893))
