# Write a loop that outputs the numbers in a list named salaries. The outputs should be 
# formatted in a column that is right-justified, with a field width of 12 and a precision of 2.

salaries = [200, 4500, 34342, 34342, 21212, 121211]
for x in salaries: 
    print("%12.2f" % x)