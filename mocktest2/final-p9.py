import csv
def f(value):
    count = 0
    with open("data.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if float(row["salary"]) >= value:
                count += 1
    return count

if __name__ == "__main__":
    print(f(9200))
    print(f(11640))
