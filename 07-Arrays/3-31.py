arr = [
    [-38, 19], 
    [5, 40],
    [-7, 11],
    [29, 16]
]

min_value = 0
max_value = 0
min_row = 0
min_col = 0
max_row = 0
max_col = 0

for r in range(len(arr)):
    for c in range(len(arr[r])):
        value = arr[r][c]

        if value < min_value:
            min_value = value
            min_row = r
            min_col = c

        if value > max_value:
            max_value = value
            max_row = r
            max_col = c

print("Smallest:", min_value, "at row", min_row, "col", min_col)
print("Largest:", max_value, "at row", max_row, "col", max_col)


