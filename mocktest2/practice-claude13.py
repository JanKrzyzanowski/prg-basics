def f(first_letter):
    with open("data.txt", "r") as file:
        content = file.read().split().strip('.,!?;:"')
        for w in file:
            if w[0] == first_letter:
                return True
            else:
                return False

if __name__ == "__main__":
    print(f("w", "d"))
