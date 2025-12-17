def f(array2D):
    # Loop through each index (0, 1, 2, ...)
    total = 0

    for i in array2D:
        total = sum(array2D[0])

    column_sum = sum(array2D[row][0] for row in range(len(array2D)))

    if column_sum == total:
        return True
    else:
        return False
    
    # For each index i:
    #   - Calculate row i sum
    #   - Calculate column i sum
    #   - If they don't match, return False immediately
    # If all matched, return True
    
if __name__ == "__main__":
    print(f([[3,7,2],[4,2,5],[5,2,1]]))  # True (all match)
    print(f([[3,7,2],[4,2,5],[9,2,1]])) 
            