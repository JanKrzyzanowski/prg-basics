def f(array2D):
    row_sum = sum(array2D[0])  # Sum of row 0
    col_sum = sum(array2D[row][0] for row in range(len(array2D)))  # Sum of column 0
    
    if row_sum == col_sum:
        return True
    else: 
        return False

    
if __name__ == "__main__":
    print(f([[3, 7, 2], [4, 2, 5], [5, 2, 1]]))  # Should print True
    print(f([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Should print False