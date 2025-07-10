'''
Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
Salary(Lakhs) : Tax(%)

Below 5 : 0%
5-10 : 10%
10-20 : 20%
aboove 20 : 30%'''


# Input CTC in lakhs
ctc_lakhs = float(input("Enter your CTC (in lakhs): "))

# Convert to rupees
salary = ctc_lakhs * 100000

# Deductions
hra = salary * 0.10
da = salary * 0.05
pf = salary * 0.03
total_deductions = hra + da + pf

# In-hand salary before tax
in_hand_salary = salary - total_deductions

# Tax calculation
if ctc_lakhs < 5:
    tax_rate = 0
elif 5 <= ctc_lakhs < 10:
    tax_rate = 0.10
elif 10 <= ctc_lakhs <= 20:
    tax_rate = 0.20
else:
    tax_rate = 0.30

# Apply tax
tax_amount = in_hand_salary * tax_rate
net_salary = in_hand_salary - tax_amount

# Monthly salary
monthly_salary = net_salary / 12

# Output
print(monthly_salary)