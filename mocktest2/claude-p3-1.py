def f(array2D):
    return sum(array2D[row][1] for row in range(len(array2D)))
    
if __name__ == "__main__":
    print(f([[3, 7, 2], [4, 2, 5], [5, 2, 1]]))  # Should print 11
    # Column 1 is: 7, 2, 2 → sum = 11