quantity=int(input("enter the Quantity:"))
price=int(input("Enter the price:"))
discount=int(input("Enter the discount(%):"))
total_cost = price * quantity
print("Total amount:",total_cost)

sellingPrice=total_cost-(total_cost*(discount/100))
print("Selling Price:",sellingPrice)

if quantity > 100:
    discount = 15
    total_after_discount =  sellingPrice- (sellingPrice * discount / 100)

    print("The total after discount is:", total_after_discount)

