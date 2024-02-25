# Author: Antony S
# Date: 2024-02-11
# Program Name:Author: Antony S
# Date: 2024-02-11
# Program Name: Population of Organisms

intial_no = int(input("Enter no of organisms:"))
rate_of_growth = int(input("Enter rate of growth:"))
no_of_hours_for_rate = int(input("Enter hours for this rate:"))
no_of_hours_for_growth = int(input("Enter hours for this growth:"))

growth_factor = rate_of_growth ** (1 / no_of_hours_for_rate)

total_population = intial_no
for i in range(no_of_hours_for_growth):
    total_population *= growth_factor




