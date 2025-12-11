first_name = input("Enter you first name: ")
last_name = input("Enter you last name: ")

first_initial = lambda first, last: first[0]  + last[0]

initials = first_initial(first_name, last_name)

print(initials)




