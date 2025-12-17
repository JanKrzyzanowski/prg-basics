def f(letter):
    with open ("data.txt","r") as file:
        content = file.read()

        words = content.split()

        count = 0
        for word in words:
            if word[0] == letter.lower():
                count += 1
        return count
        

if __name__ == "__main__":
    print(f("w"))