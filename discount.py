quantity=int(input("enter the Quantity:"))
price=int(input("Enter the price:"))
discount=int(input("Enter the discount(%):"))

total_before_discount = price * quantity
print("The total before discount is:", total_before_discount)
total_after_discount = total_before_discount - (total_before_discount * discount / 100)
print("The total after discount is:", total_after_discount)
