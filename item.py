ItemList = ["Biryani", "Malai Tikka", "Butter Naan", "Butter Chicken", "Kabaab", "Tikka", "Soft drink", "Gulab Jamun"]
UnitPrice = [150, 60, 20, 100, 30, 50, 20, 50]
Discount = [5, 10, 15, 20, 5, 10, 5, 10]

print("Item List:")
for i in range(len(ItemList)):
    print(f"{i+1}. {ItemList[i]}")

TotalPrice = 0
Choice = 'y'

while Choice == 'y':
    Choice = input("Do you have more items to buy? (y/n): ")
    
    if Choice == 'y':
        while True:
            try:
                ItemIndex = int(input("Which item? (1-8): ")) - 1
                if 0 <= ItemIndex < len(ItemList):
                    break
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        while True:
            try:
                Qty = int(input("Quantity: "))
                if Qty > 0:
                    break
                else:
                    print("Invalid quantity. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        Price = UnitPrice[ItemIndex] * Qty
        DiscountAmount = (Price * Discount[ItemIndex]) // 100
        TotalPrice += Price - DiscountAmount
        print(f"You have added {Qty} {ItemList[ItemIndex]}(s) to your cart.")
        print(f"Discount: {DiscountAmount}")
        print(f"Total amount to Pay: {TotalPrice}")
    
    elif Choice == 'n':
        print(f"Total amount to Pay: {TotalPrice}")
        break
    
    else:
        print("Invalid input. Please enter y or n.")
if TotalPrice>1000:
    discount=5
    total_after_discount =  TotalPrice-(TotalPrice*discount//100)
    print("The total after discount is:", total_after_discount)

