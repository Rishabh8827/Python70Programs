'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Write a program to input electricity unit charges and calculate total electricity bill according to the given  condition:********\n\n")
units = int(input("Please Enter The Number oOf Units You Consumed In A Month : "))
bill = 0.0
if(units > 0 and units <= 50): bill = units*0.50
elif(units > 50 and units <= 150): bill =  (50*(0.50)) + (units - 50)*0.75
elif(units > 150 and units <= 250): bill = (50*(0.50)) + (100*0.75) + (units - 150)*1.20
elif(units > 250): bill = (50*(0.50)) + (100*0.75) + (100)*1.20 + (units - 250)*1.50

bill = bill + ((bill*20)/100) #20% surCharge
print("Your Electricity Bill Is : ", bill)


































































#Name Rishabh Patel