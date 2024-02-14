# lower bound to upper bound sum 
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
theSum = 0
for x in range(lower, upper+1):
    theSum += x

print(theSum)