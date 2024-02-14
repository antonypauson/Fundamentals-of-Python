# finding the sum of even numbers of upto a number
endNum = int(input("Enter the number: "))
theSum = 0
for x in range(0,endNum,2):
    theSum += x 

print(theSum)