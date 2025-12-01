arr= [
    2, 3, 2, 5, 8, 1, 9, 8
]


print('Array: ', end = ' ',)
for number in arr:
    print(number, end=" ")   
print()



print("Unique elements:", end=" ")
number = 0
for number in arr:
    if number % 2 != 0:
        print(number, end=" ")