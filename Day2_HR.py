#meal cost
# tip cost
# tax cost


# meal = float(input('Please enter the price of the item: '))
# tip = int(input('Please enter the tip %: '))
# tax = int(input('Please enter the tax percentage: '))
#
# final_cost = meal +(tip/100)*meal + (tax/100)*meal

print(round(final_cost))





def total_cost():
    meal = float(input('Please enter the price of the item: '))
    tip = int(input('Please enter the tip %: '))
    tax = int(input('Please enter the tax percentage: '))
    final_cost = round(meal +(tip/100)*meal + (tax/100)*meal)
    return str(final_cost)

print('So the total cost is ' + total_cost() + '$')

