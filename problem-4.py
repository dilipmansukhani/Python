'''
`Problem 4`: Write a menu-driven program - 
1. cm to ft 
2. km to miles 
3. USD to INR 
4. exit
'''

a = int(input("""Menu:
1. cm to ft 
2. km to miles 
3. USD to INR 
4. Exit
Enter your choice (1-4): """))

if a == 1:
    x = float(input("Enter the number in cm: "))
    ft = x * 0.0328084
    print(f"{x} cm = {ft:.2f} feet")

elif a == 2:
    x = float(input("Enter the number in km: "))
    miles = x * 0.621371
    print(f"{x} km = {miles:.2f} miles")

elif a == 3:
    x = float(input("Enter the amount in USD: "))
    inr = x * 83.0  # Update the rate as needed
    print(f"${x} = ₹{inr:.2f}")

elif a == 4:
    print("Exiting the program. Thank you!")

else:
    print("Invalid choice! Please select a valid option (1 to 4).")
