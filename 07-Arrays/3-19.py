arr = [
    1, 2, 4, 5, 6
]

number = int(input('Enter your number: '))
x=0
for element in arr:
    if number > element:
        x += 1
    elif number < element:
        print("Your number is bigger than ",x, "values")

