import json

def f(age):
    with open("data.json", "r") as file:
        data = json.load(file)

    count = 0    
    for student in data:
        if student["age"] == age:
            count += 1
    return count

if __name__ == "__main__":
    print(f(25))