def calculate_discount(purchase_amount):
    if purchase_amount >= 5000:
        discount = purchase_amount * 0.20
    elif purchase_amount >= 3000:
        discount = purchase_amount * 0.10
    elif purchase_amount < 300:
        discount = purchase_amount * 0.05
    else:
        discount = 0

    payable_amount = purchase_amount - discount
    return discount, payable_amount


purchase_amount = float(input("Enter the purchase amount in rupees: "))
discount, payable_amount = calculate_discount(purchase_amount)
print(f"Discount: Rs {discount:.2f}")
print(f"Payable amount: Rs {payable_amount:.2f}")