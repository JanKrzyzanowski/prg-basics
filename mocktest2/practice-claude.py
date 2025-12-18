def f(array):
    count = 0 
    for numbers in set(array):
        if array.count(numbers) == 1:
            count += numbers
    return count
    
if __name__ == "__main__":
    # Test with the examples
    print(f([5,5,5,3,5,8,5]))  # Should print 11
    print(f([7,7,7,7,7,5,7,7]))