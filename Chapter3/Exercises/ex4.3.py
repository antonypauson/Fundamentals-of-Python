# The log 2 of a given number N is given by M in the equation N=2^M . Using integer 
# arithmetic, the value of M is approximately equal to the number of times N can be 
# evenly divided by 2 until it becomes 0. Write a loop that computes this approximation of the log 2 of a given number N. You can check your code by importing the 
# math.log function and evaluating the expression round(math.log(N, 2)) (note 
# that the math.log function returns a floating-point value)
#8 = 2^3
n = int(input("Enter the number:"))
count = -1
while n >= 1:
    n = n / 2
    count += 1
print(count)

