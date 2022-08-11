
annual_salary= float(input('Enter your annual salary: '))
portion_saved= float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost= float(input('Enter cost of dream home: '))
semi_annual_raise= float(input('Enter the semi­annual raise, as a decimal: '))

r= 0.04 #annual return on investments
current_savings=0
portion_down_payment = 0.25 * total_cost
number_of_months = 0



while current_savings < portion_down_payment:

    current_savings += (current_savings*r/12) + ((annual_salary/12) * portion_saved)
    number_of_months += 1

    if number_of_months>= 6 and (number_of_months%6) == 0:
        annual_salary += annual_salary*semi_annual_raise


print(number_of_months)