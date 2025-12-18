def f(subject):
    return max(subject, key = lambda s: sum((subject[s])) / len(subject[s]))
if __name__ == "__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))