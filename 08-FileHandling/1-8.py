def read_from_file(name):
    with open(name) as file:
        content = file.read()
    return content

file_content = read_from_file("pets.txt")
file_lines = file_content.splitlines()

total_words = 0
for line in file_lines:
    words = line.split()
    total_words += len(words)

print('The total number of words in the text are: ', total_words)

