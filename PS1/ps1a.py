# total_cost = cost of dream house
# portion_down_payment = portion of the cost needed for a down payment (=0.25)
# current_savings = amount saved thus far (=0 $)
# r = annual return (return of investments = 0.04)
# every month I recieve an additional current_savings*r/12
# annual_salary
# portion_saved (from salary every month) (decimal form)
# at the end of every month savings increase by return on investments plus percentage of monthly salary

annual_salary= float(input('Enter your annual salary: '))
portion_saved= float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost= float(input('Enter cost of dream home: '))

r= 0.04 #annual return on investments
current_savings=0
portion_down_payment = 0.25 * total_cost
monthly_salary = annual_salary / 12
number_of_months = 0

while current_savings < portion_down_payment:
    current_savings += (current_savings*r/12) + (monthly_salary * portion_saved)
    number_of_months += 1
print(number_of_months)