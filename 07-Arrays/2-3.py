# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food_expense=0
trans_expense=0
uti_expense=0

for week in monthly_expenses:
    food_expense += week[0]
    trans_expense += week[1]
    uti_expense += week[2]

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food_expense )
print('Transport:', trans_expense)
print('Utilities:', uti_expense)
print('Week 1:',sum(monthly_expenses[0]))
print('Week 2:',sum(monthly_expenses[1]))
print('Week 3:',sum(monthly_expenses[2]))
print('Week 4:',sum(monthly_expenses[3]))
print('---------------')
print('TOTAL: ',food_expense + trans_expense + uti_expense)