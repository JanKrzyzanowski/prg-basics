arr= [
    7,9,2,4,5,6
]

j = 0

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[i], arr[j] = arr[j], arr[i]
        j+=1
print(arr)

