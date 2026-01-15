def f(first_letter,last_letter):
    count = 0
    with open("data.txt", "r") as file:
        content = file.read().split()
        for w in content:
            if w.startswith(first_letter) and w.endswith(last_letter):
                count += 1
    return count

if __name__ == "__main__":
    print(f("w", "d"))