current_price= float(input("Enter current price: "))
previous_price= float(input("Enter previous price: "))

price_change= previous_price - current_price
percentage_drop= (price_change/previous_price)*100

if percentage_drop >= 10:
    print('Buy the product!')
    print(f'Product price reduced by {int(percentage_drop)}%')
else:
    print('Dont buy the product')