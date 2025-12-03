arr = [
    1, 2, 4, 5, 6
]

number = float(int(input('Enter your number: ')))
x=0
for element in arr:
    if element > number:
        x += 1
    
print("There are",x, "values in the element bigger than your number")

 