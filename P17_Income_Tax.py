'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Write a program to Calculate income tax for the given income by adhering to the rules********\n\n")
income = int(input("Please Enter Your Current Income : "))

incomeTax = 0

if(income > 0 and income <= 100000):print("\nYour incomeTax Is : ",incomeTax)
elif(income > 100000 and income <= 200000):incomeTax = income/10; print("\nYour incomeTax Is : ",incomeTax)
else:incomeTax = income/20; print("\nYour incomeTax Is : ",incomeTax)

































































#Name Rishabh Patel