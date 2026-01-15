import json

def f(years, course, average_grade):
    with open("data.json", "r") as file:
        data = json.load(file)

    count = 0 
    for student in data:
        if student ["age"] >= years:
            for c in student["studies"]["courses"]:
                if c["name"] == course:
                    

if __name__ == "__main__":
    print(f(21, "statistics", 4))