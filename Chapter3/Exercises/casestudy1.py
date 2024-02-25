startBal = float(input("Enter the investment amount:"))
noYears = int(input("Enter the number of years:"))
intRate = int(input("Enter the rate as in %"))
# Input the starting balance, number of years, and interest rate
# Set the total interest to 0.0
# Print the table's heading
# For each year
#  compute the interest
#  compute the ending balance
#  print the year, starting balance, interest, and ending balance
#  update the starting balance
#  update the total interest
# print the ending balance and the total interest
totalInterest = 0.0
print("%4s%18s%10s%16s" % ("Year","Starting balance","Interest", "Ending balance"))
for x in range(1,noYears+1):
    interest = startBal * intRate
    endBalance = startBal + interest
    print("%4d%18.2f%10.2f%16.2f" % \
    (x, startBal, interest, endBalance))
    startBal = endBalance
    totalInterest += interest

print("Total Interest ", totalInterest)
print("End Balance ", endBalance)