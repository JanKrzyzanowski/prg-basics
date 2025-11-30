arr= [
    15, 8, 31, 47, 2, 19
]

print(arr)

x=0
y= len(arr)

for numbers in arr:
    x += numbers
    numbers = x/y
print("Arithmetic average: ",numbers)