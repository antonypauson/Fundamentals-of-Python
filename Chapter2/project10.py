"""
Author: Antony S
Date: 2024-02-11
Program: 
An employee’s total weekly pay equals the hourly wage multiplied by the total 
number of regular hours plus any overtime pay. Overtime pay equals the total 
overtime hours multiplied by 1.5 times the hourly wage. Write a program that 
takes as inputs the hourly wage, total regular hours, and total overtime hours and 
displays an employee’s total weekly pay."""
hourlyWage = int(input("Enter the hourly wage: "))
total_regular_hours = int(input("Enter total regular hours: "))
total_overtime_hours = int(input("Enter total overtime hours: "))
overtime_pay = total_overtime_hours * 1.5 * hourlyWage
weekly_pay = hourlyWage * total_regular_hours + overtime_pay
print("Total Weekly Pay = ",weekly_pay)
