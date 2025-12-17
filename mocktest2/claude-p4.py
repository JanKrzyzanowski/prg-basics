def f(subjects):
    return min(subjects, key = lambda s: sum(subjects[s])/ len(subjects[s]))
    
if __name__ == "__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))  # Should print "math"