def f(c):
    order = "AKQJT98765432"
    return "".join(sorted(c, key = lambda s: order.index(s)))

if __name__ == "__main__":
    print(f("73TQ"))
    print(f("7K3A9"))