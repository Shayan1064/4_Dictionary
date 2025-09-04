cart = {}
total_price=0
while True:
    key = input("Enter Item name OR type 'Q' to EXIT!: ")
    if key.lower() == "Q".lower():
        break
    value = int(input("Enter Item Price: "))
    cart[key] = value
    total_price+=value
    for name,price in cart.items():
        print(name," ",price)

    print("Total Price : ",total_price)

