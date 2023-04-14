# find the factorial of an integer using function

def fact(num):

    if num == 1:
        out = 1
        return out
    else:
        out = (num*fact(num-1))
        return out


x=10
print("factorial of ",x, "is",fact(x))

