stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

total_value = sum(list(map(lambda product: product[0] * product[1], stock)))

print("Products in stock:", stock)
print(f"Total value: {total_value}")

