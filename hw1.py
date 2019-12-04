# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:11:47 2019

@author: vrlpa
Part A: Calculating total amount owed after graduation (2 points)

•	Use input() to set variables float variables loan_per_year and interest_rate and int variable years.
•	You will need two other variables:
o	total_owed = 0
o	counter = 0   (This is a counter variable to count how many times the loop has been executed)
•	Construct a while loop that calculates how much you will owe by graduation.
•	Each year, you will add the loan_per_year to your total_owed and multiply by the interest_rate
•	The while loop will end when your counter is equal to your years.
Example input:
Number of years: 4

Loan amount per year: 4000

Interest rate (Ex. 0.045 for 4.5% annual): .05 

Example output:
Total Owed At Graduation
$ 18102

"""
#Part A
loan_per_year = float(input('Enter your loan amount per year: '))
interest_rate = float(input('What is your interest rate? '))
years = int(input('For how many years? '))
counter = 0
total_owed = 0
while counter != years:
    counter += 1
    total_owed += loan_per_year+ ((loan_per_year + total_owed)*interest_rate)
    #Since we take a loan out each year I added loan per year to the given formula
print('Total amount owed at graduation ' + str(int(total_owed)))

"""
Part B: Determine if monthly payment is feasible (1 point)

•	Below the code for Part A, use input() to set float variable monthly_payment.
•	Use if/else logic to check if the monthly payment would be possible.
 For example, if your interest accrued each month is more than your monthly payment,
 then you would be paying off your loan forever.  
 Print whether it is possible with the monthly payment entered as well as 
 the minimum monthly payment needed to not have your loan grow.

(Hint: Your monthly interest rate is your annual interest rate divided by 12.)
Example input:
Name a monthly payment: 300

Name a monthly payment: 50

Example output:
A monthly payment of $300 will work!
The minimum monthly payment for this loan would be 75 dollars.

A monthly payment of $50 won’t work! You’ll be paying off your loans forever.
The minimum monthly payment for this loan would be 75 dollars.

"""
#Part B
monthly_payment = float(input('Enter your monthly payment: '))

monthly_interest_rate = (interest_rate/12) #interst rate per month
minimum_payment = monthly_interest_rate*total_owed 
#minimum payment is caluculated by finding the
if minimum_payment > monthly_payment:
    print('You are going to pay your loan forever!')
    
else:
    print('This monthly payment will help you pay off your loan!')
    
print('The minimum monthly payment for this loan is '+str(int(minimum_payment))+' dollars')

"""
Part C: Determine how long it will take to pay off your student loans (2 points
•	Using your variable monthly_payment from Part B, now calculate how long it will take to
 pay off your student loans.
•	Use a while loop that will continue to run until the total_owed is less than or equal to 0.
•	You will also need an integer counter variable month that keeps track of how many months 
have passed (how many times the loop is run)
•	In the loop,
o	Subtract the monthly payment
o	Add back interest accrued that month
o	Add one to the counter variable month

Print out the number of months and years it will take to pay off the loans.
 Note, you do not need to count partial months and the number of years do not 
 need to be formatted.

Example output:
	It will take 70 months to pay off your student loans.
It will take 5.833333333333333 years to pay off your student loans.

"""
#Part C
counter_month = 0
while total_owed >= 0:
    counter_month += 1
    counter_year = (counter_month/12)
    total_owed = (total_owed - monthly_payment)
    total_owed = (total_owed * monthly_interest_rate)+total_owed
    
print('You will have to pay your loans for '+ str(counter_month)+' months')

print('In the other words '+ str(int(counter_year))+' years')