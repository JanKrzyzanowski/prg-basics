arr1=[
    9, 6, 10
]

arr2= [
    1, 2, 3, 4, 5, 6
]

is_subset = True

for x in arr1:
    if x not in arr2:
        is_subset= False

if is_subset:
    print('arr1 is a subset of arr2')
else:
    print('arr1 is not a subset of arr2')
