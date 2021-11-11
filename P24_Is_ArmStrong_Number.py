'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Program to check whether a given number is an Armstrong number or not.********\n\n")
num = input("\tEnter The Number To Check Armstrong number : ")
ArmStrong = 0
inNumber = int(num)
strlen = len(num)
for i in range(strlen):
    ArmStrong = ArmStrong + int(num[i])**strlen
if(inNumber == ArmStrong): print("\n\tThe Given Number Is \"ArmStrong Number\" : ", inNumber," = ", ArmStrong)
else: print("\n\tThe Given Number Is \"Not ArmStrong Number\" : ", inNumber ," != ", ArmStrong)



































































#Name Rishabh Patel