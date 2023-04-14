
def get_cube(num):
    result = num*num*num
    return result

for i in range(1,11):
    sq = get_cube(i)
    print("Cube of ",i,"is",sq)