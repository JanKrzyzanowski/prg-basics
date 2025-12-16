def f(array2D):
    n = len(array2D)

    for i in range(n):
        # Calculate sum of row i
        row_sum = sum(array2D[i])
        
        # Calculate sum of column i
        column_sum = sum(array2D[row][i] for row in range(n))
        
        # If they don't match, return False
        if row_sum != column_sum:
            return False
    
    # If all matched, return True
    return True

if __name__ == "__main__":
    print(f([[3,7,2],[4,2,5],[5,2,1]]))  
    print(f([[3,7,2],[4,2,5],[9,2,1]]))

            