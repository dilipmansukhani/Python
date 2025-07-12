'''
Problem 3: Write a program that will take user input of cost price and selling price and determines
 whether its a loss or a profit.'''

cost_price = int(input("Enter the buying price: "))
selling_price = int(input("Enter the selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"Profit of ₹{profit}")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f"Loss of ₹{loss}")
else:
    print("No profit, no loss")
  