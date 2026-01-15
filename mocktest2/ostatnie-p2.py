def f(arr):
    count = 0
    for number in set(arr):
        if arr.count(number) == 1:
            count += number
    return count
    
if __name__ == "__main__":
 print( f([7,7,7,7,7,5,7,7]) )
 