def f(arr):

    total = 0
    
    for number in set(arr):  # set removes duplicates!
        if arr.count(number) == 1:
            total += number
    
    return total

if __name__ == "__main__":
    print(f([5, 5, 5, 5, 3, 5, 8, 5]))  # Should print 11
    print(f([9, 9, 2, 9, 9, 9, 7]))     # Should print 9
    print(f([1, 4, 4, 4, 4, 6, 4])) 
