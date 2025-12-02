tuple = (50, 20, 40, 50, 30, 50)

print('Tuple: ', *tuple)

value = (50)
x=0 
print('Value: ', value)

for element in tuple:
    if element == value:
        x += 1

print("Number of occurences: ", x)