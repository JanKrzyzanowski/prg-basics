import json

def f(years, course, average_grade):
    with open("data.json", "r") as file:
        data = json.load(file)

    count = 0
    for student in data:
        # Check age
        if student["age"] >= years:
            # Loop through courses in studies
            for c in student["studies"]["courses"]:
                # Check if this is the course we're looking for
                if c["name"] == course:
                    # Calculate average
                    grades = c["grades"]
                    avg = sum(grades) / len(grades)
                    
                    # Check if average meets requirement
                    if avg >= average_grade:
                        count += 1
                    break  # Found the course, stop looking
    
    return count
    
if __name__ == "__main__":
    print(f(21, "statistics", 4))