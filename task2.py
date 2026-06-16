stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 200
}

name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if name in stocks:
    price = stocks[name]
    total = price * quantity

    print("Stock Name:", name)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total Investment =", total)

else:
    print("Stock not found")