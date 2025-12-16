def f(arr):
    for number in set(arr):
        if arr.count(number) == 1:
            return number

if __name__ == "__main__":
    print(f([4, 7, 4, 7, 4, 9, 7]))  # Should print 9
    print(f([1, 1, 1, 5, 5, 5, 3, 8, 8, 8]))  # Should print 3
    print(f([2, 2, 2, 6, 6, 6, 10, 10, 10, 15]))