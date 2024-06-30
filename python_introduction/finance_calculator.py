month = int(input("Enter your monthly income: "))
T_month = int(input("Enter your total monthly expenses: "))
monthly_savings = month-T_month
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are ${} .".format(monthly_savings))
print("Projected savings after one year, with interest, is: ${} .".format(Projected_Savings))
