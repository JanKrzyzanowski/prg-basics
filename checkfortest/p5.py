def f(shopping_cart, price_list, customer_wallet):
    total = 0
    for product, quantity in shopping_cart.items():
        if product in price_list:
            total += price_list[product] * quantity
        else:
            return False
    return total <= customer_wallet

if __name__ == "__main__":
    print(f())
    print(f())
    print(f())