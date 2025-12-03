def create_2d_arr(x,y):
    return [[0]* y for x in range(x)]

row = 2
coms = 3

arr = create_2d_arr(row,coms)

for row in arr:
    print(row)

