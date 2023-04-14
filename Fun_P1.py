# program to find sum of multiple numbers

def sum_all(*num):
    result = 0

    for i in num:
        result = result+i
        return result


x=sum_all(23,6,8,38)
print("sum of all number is : ",x)