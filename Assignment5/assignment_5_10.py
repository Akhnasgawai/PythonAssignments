"""10"""
salary = int(input("Enter your salary: "))
year = int(input("Enter the total no years you served the company: "))
if year > 5:
    bonus = salary * 0.05
    salary += bonus
print("Net Salary after bonus: ", salary)
