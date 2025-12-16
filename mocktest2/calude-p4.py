def f(students):
    return min(students, key=lambda name: sum(students[name]) / len(students[name]))

if __name__ == "__main__":
    print(f({"Alice": [85, 90, 88], "Bob": [70, 75, 72], "Charlie": [95, 92, 94]}))
    print(f({"Emma": [100, 95], "Liam": [88, 92, 85], "Sophia": [90, 90]}))