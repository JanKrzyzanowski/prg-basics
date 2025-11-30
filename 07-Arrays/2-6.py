arr =[
   [0,0,0],
   [0,0,0],
   [0,0,0]
]




for number in range(len(arr)):
    arr[number][number] = 1

for row in arr:
    for value in row:
        print(value, end=' ')
    print()