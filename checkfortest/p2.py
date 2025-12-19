def f(a,b):
    x, y = 0,1
    total = 0

    while y<=b:
        if y >= a:
            total += y
        x,y = y,x + y
    
    return total

if __name__ == "__main__":
    print(f(1,5))
    
