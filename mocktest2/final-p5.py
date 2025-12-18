def f(first_letter, last_letter):
    with open("data.txt", "r", encoding="utf-8") as file:
        words = file.read().split()

    first_letter = first_letter.lower()
    last_letter = last_letter.lower()

    return sum(
        w.lower().startswith(first_letter) and w.lower().endswith(last_letter)
        for w in words
    )


if __name__ == "__main__":
    print(f("w", "d"))