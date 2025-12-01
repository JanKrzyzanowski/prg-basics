def compare(array1, array2):
    
    if len(array1) != len(array2):
        return False
    
    
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    
    return True
        

array1= [
   "water", "book", "sky"
]

array2=[
   "water", "book", 'sky'
]

print(array1)
print(array2)

