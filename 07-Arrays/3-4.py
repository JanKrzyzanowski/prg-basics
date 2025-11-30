arr= [
    -15, 8, -31, 47, -2, 19
]

min= arr[0]
max= arr[0]

for number in arr:
    if number < min:
        min = number

for number in arr:
    if number > max:
        max = number

print("Min: ",min)
print("Max: ", max)