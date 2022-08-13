######################
# User input and initializing variables
######################

a= float(input('Enter your annual salary: '))
total_cost= 1000000
semi_annual_raise= 0.07
annual_salary=a

r= 0.04 #annual return on investments
current_savings=0 #should be within 100$ of portion_down_payment
portion_down_payment = 0.25 * total_cost

num_steps=0
low=0
high=10000
number_of_months = 0
guess=(high+low)/2
portion_saved=guess/10000

is_it_enough=False

######################
# Checking if salary is enough at a 100% savings rate
######################

for x in range(36):

        current_savings += (current_savings*r/12) + (annual_salary/12)

        if number_of_months>= 6 and (number_of_months%6) == 0:
            annual_salary += annual_salary*semi_annual_raise
        number_of_months+=1

if current_savings < portion_down_payment:
    print('It is not possible to pay the down payment in three years.')
else:
    is_it_enough=True

######################
# Bisection search
######################


number_of_months = 0
annual_salary=a
current_savings=0

while abs(current_savings - portion_down_payment) >= 100 and is_it_enough==True:

    number_of_months = 0
    annual_salary=a
    current_savings=0
    for i in range(36):

        current_savings += (current_savings*r/12) + ((annual_salary/12) * portion_saved)

        if number_of_months>= 6 and (number_of_months%6) == 0:
            annual_salary += annual_salary*semi_annual_raise
        number_of_months+=1


    if current_savings < portion_down_payment:
        low=guess
    else:
        high=guess


    guess=(high+low)/2
    portion_saved=guess/10000
    num_steps += 1

if is_it_enough==True:
    print('Best savings rate: ', portion_saved)
    print('Steps in bisection search: ', num_steps)