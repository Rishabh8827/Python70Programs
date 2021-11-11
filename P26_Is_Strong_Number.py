'''
Name - Rishabh Patel
Branch - Computer Engineering(CO)
Roll No. - 0827CO191046

'''

print("\t\t********Program to check whether a given number is an Strong number or not.********\n\n")
num = input("\tEnter The Number To Check Strong number : ")
Strong = 0
factorial = 1
inNumber = int(num)
strlen = len(num)
for i in range(strlen):
    for j in range(1,int(num[i])+1):
        factorial = factorial*j
    Strong = Strong + factorial
    factorial = 1
if(inNumber == Strong): print("\n\tThe Given Number Is \"Strong Number\" : ", inNumber," = ", Strong)
else: print("\n\tThe Given Number Is \"Not Strong Number\" : ", inNumber ," != ", Strong)



































































#Name Rishabh Patel