"""9"""
quantity = int(input("Enter the quantity: "))
price = quantity * 100
if price > 1000:
    discount = price * 0.1
    price -= discount
print(price)
