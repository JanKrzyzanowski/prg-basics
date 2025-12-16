def f(arr):
    for number in set(arr):
        if arr.count(number):
            return number


if __name__ == "__main__":
    print(f([7,7,7,7,7,5,7,7]))  
    