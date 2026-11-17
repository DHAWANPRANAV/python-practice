#A sales analyst receives revenue values as string inputs from the user. Ask the user to 
#enter revenue for three months, convert them to floats, and calculate total and average 
#revenue.

revenue1 = float(input("Enter revenue for month 1: "))
revenue2 = float(input("Enter revenue for month 2: "))
revenue3 = float(input("Enter revenue for month 3: "))

total_revenue = revenue1 + revenue2 + revenue3
average_revenue = total_revenue / 3

print("Total Revenue:", total_revenue)
print("Average Revenue:", round(average_revenue,2))

