arr= [
    15, 8, 31, 47, 2, 19
]

print(arr)

numbers = 0
y=len(arr)
total=0
while numbers < y:
    total += arr[numbers]
    numbers += 1


average = total / y
print(average)
    