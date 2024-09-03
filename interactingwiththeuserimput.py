# This is all asking for all the numbers of evrerything 
Budget = float(input("Enter budget total: "))
Housing = float(input("Enter housing budget: "))
Utilities = float(input("Enter utilities budget: "))
groceries = float(input("Enter groceries budget: "))
Transportation = float(input("Enter Transportation budget: "))
HealthCare = float(input("Enter Health Care budget: "))
PersonalCare = float(input("Enter Personal Care budget: "))
Clothing = float(input("Enter Clothing budget: "))
Debt = float(input("Enter debt budget: "))

# Finds the housing budget by Housing/Budget
HousingBudget = Housing/Budget
print(f"The percent of budget taken up by housing {HousingBudget:.2f}")
#finds the utilities budget by Utilities/Budget
UtilitiesBudget = Utilities/Budget
print(f"The percent of budget taken up by Utilities {UtilitiesBudget:.2f}")
#finds the groceries budget by groceries/Budget
groceriesBudget = groceries/Budget
print(f"The percent of budget taken up by groceries {groceriesBudget:.2f}")
#finds the transportation budget by Transportation/Budget
TransportationBudget = Transportation/Budget
print(f"The percent of budget taken up by Transportation {TransportationBudget:.2f}")
#finds the health care budget by HealthCare/Budget
HealthCareBudget = HealthCare/Budget
print(f"The percent of budget taken up by Health care {HealthCareBudget:.2f}")
#finds the personal care budget by PersonalCare/Budget
PersonalcareBudget = PersonalCare/Budget
print(f"The percent of budget taken up by Personal care{PersonalcareBudget:.2f}")
#finds the clothing budget and prints by Clothing/Budget
ClothingBudget = Clothing/Budget
print(f"The percent of budget taken up by Clothing {ClothingBudget:.2f}")
#finds the debt budget and prints by Debt/Budget
DebtBudget = Debt/Budget
print(f"The percent of budget taken up by Debt {DebtBudget:.2f}")