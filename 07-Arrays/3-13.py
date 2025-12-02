def occurs(number, array):
    if number in array:
        return True
    return False


number = (23)

array=[
    15, 38, 7, 23, 14
]

print('Number: ', number)



print('Array: ', end = ' ')
for element in array:
    print(element, end = ' ')
print ()




if occurs(number,array):
    print('Result: ', number, " appears in the array")

elif number not in array:
    print ("Result: ", number, 'does not appear in the array')