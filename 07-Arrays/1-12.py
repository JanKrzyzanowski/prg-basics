categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

food_cost= expenses[0]
print("Total food cost: ", food_cost)

transport_cost= expenses[1]
print("Total food cost: ", transport_cost)

rent_cost= expenses[2]
print("Total food cost: ", rent_cost)

entertainment_cost= expenses[3]
print("Total food cost: ", entertainment_cost)

max_expense = max(expenses)
max_index = expenses.index(max_expense)

print(f"The highest cost was in {categories[max_index]}: {max_expense}")