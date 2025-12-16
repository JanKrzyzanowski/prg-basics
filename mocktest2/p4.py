def f(subjects):
    return max(subjects, key=lambda subject: sum(subjects[subject]) / len(subjects[subject]))
        
if __name__ == "__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))