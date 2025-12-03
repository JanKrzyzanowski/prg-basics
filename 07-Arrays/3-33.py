arr = [
    [4, 9, -1, 7, 3],
    [12, 0, 5, -6, 8],
    [2, 14, 11, -3, 10]
]


print("Before the swap: ")
for row in arr:
    for number in row:
        print(number, end = " ")
    print() 

for r in range(len(arr)):
    arr[r][0], arr[r][-1] = arr[r][-1],arr[r][0]

print("After the swap: ")
for row in arr:
    for number in row:
        print(number, end = " ")
    print()