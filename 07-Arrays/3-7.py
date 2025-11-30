names = [
    "Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"
]


print("Names:", end=" ")
for n in names:
    print(n, end=" ")
print()


longest = names[0]
max_len = len(names[0])

for name in names:
    if len(name) > max_len:
        max_len = len(name)
        longest = name

print("Longest name:", longest)
    