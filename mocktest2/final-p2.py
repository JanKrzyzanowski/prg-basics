def f(arr):
    count = 0
    for numbers in set(arr):
        if arr.count(numbers) == 1:
            count += numbers
    return count
    
if __name__ == "__main__":
 print( f([7,7,7,7,7,5,7,7]) )
 